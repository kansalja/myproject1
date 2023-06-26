import datetime, dateutil, re, logging
from dateparser import parse
from dateparser_data.settings import default_parsers
from django.contrib.gis.geos import Point
from dateutil.parser import ParserError
from .color_factory import ColorFactory
from geopy.geocoders import Nominatim
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

logger = logging.getLogger("django")


class PostProcess:
    """
    Class to process the data to produce
    standardised input for the model fields
    """

    _location_entity_class_types = []
    _data = []
    _source = ""

    def __new__(cls, data=[], source=""):
        obj = super().__new__(cls)
        obj._data = data
        obj._source = source
        """
        Note: "PLACE" is custom class type added in NUFORC reshaped data,
        used to signify a value that was obtained 
        from the *structured* NUFORC data & distinguish it from LOC & GPE
        entities extracted by NER from *unstructured* text.
        """
        obj._location_entity_class_types = [
            "GPE",
            "LOC",
            "PLACE",
        ]
        return obj._process()

    def _process(self):
        # function to initiate the processing functions
        _processed_docs = []
        logger.info(f"Running post-processing for {self._source['source_name']} data.")
        for doc in self._data:  # for every document
            # REDDIT data
            if self._source["source_name"] == "REDDIT":
                # attribute data to variables - default structure
                obs_dates = self._process_dates(
                    [e[0] for e in doc["entities"] if e[1] == "DATE"]
                )[0]
                obs_times = self._process_times(
                    [e[0] for e in doc["entities"] if e[1] == "TIME"]
                )[0]
                source_name = self._source["source_name"]
                source_url = self._process_source_url(doc["report_link"])
                obs_txt = self._process_text(doc["text"])
                obs_types = self._process_types(
                    [e[0] for e in doc["entities"] if e[1] == "TYPE"]
                )
                obs_colors = self._process_colors(
                    [e[0] for e in doc["entities"] if e[1] == "COLOR"]
                )
                obs_locs = self._process_locs(
                    [
                        e
                        for e in doc["entities"]
                        if any(t == e[1] for t in self._location_entity_class_types)
                    ]
                )
            # NUFORC data
            elif self._source["source_name"] == "NUFORC":
                doc = self._reshape_nuforc_data(doc)  # reshape data for NUFORC
                source_name = self._source["source_name"]
                source_url = self._process_source_url(doc["report_link"])
                obs_txt = self._process_text(doc["text"])
                obs_dates = self._process_dates([doc["date_time"]])[0]
                obs_times = self._process_times([doc["date_time"]])[0]
                obs_types = self._process_types(
                    [e[0] for e in doc["entities"] if e[1] == "TYPE"]
                ) + [doc["shape"]]
                obs_colors = self._process_colors(
                    [e[0] for e in doc["entities"] if e[1] == "COLOR"]
                )
                obs_locs = self._process_locs(
                    [
                        e
                        for e in doc["entities"]
                        if any(t == e[1] for t in self._location_entity_class_types)
                    ]
                )
            # add results to list
            _processed_docs.append(
                {
                    "source_name": source_name,
                    "source_url": source_url,
                    "obs_txt": obs_txt,
                    "obs_types": obs_types,
                    "obs_colors": obs_colors,
                    "obs_dates": obs_dates,
                    "obs_times": obs_times,
                    "obs_locs": obs_locs,
                }
            )
        return _processed_docs

    # reshape NUFORC location data to make it consistent with other source types
    def _reshape_nuforc_data(self, doc):
        doc["entities"].append(
            (
                f"{doc['city'] if doc['city'] else ''}, {doc['state'] if doc['state'] else ''}",
                "PLACE",
            )
        )
        return doc

    # process observation types
    def _process_colors(self, colors=[]):
        formatted = []
        for color in colors:
            s = Scrubbers(color)
            color = s.run_color_scrubbers()
            if color:
                formatted.append(color)
        return list(set(formatted))

    # process observation types
    def _process_types(self, types=[]):
        formatted = []
        for type in types:
            s = Scrubbers(type)
            type = s.run_type_scrubbers()
            formatted.append(type)
        return list(set(formatted))

    # process place name. Returns list [{"place_name": "name string", "coordinates": Point(longitude,latitude)})]
    def _process_locs(self, locs=[]):
        return ProcessLocations(data=[loc[0] for loc in locs], geocode=True)

    # process date from strings & return list of datetime.date objects
    def _process_dates(self, date_strings=[]):
        formatted = []
        discarded = []
        for date in date_strings:
            try:
                parsers = [
                    parser for parser in default_parsers if parser != "relative-time"
                ]
                parsed = parse(
                    date,
                    settings={"PARSERS": parsers, "REQUIRE_PARTS": ["day", "month"]},
                )
                if parsed and parsed <= datetime.datetime.today():
                    formatted.append(parsed)
                else:
                    discarded.append(date)
            except ParserError:
                discarded.append(date)
        return list(set(formatted)), discarded

    # process time from strings & return list of datetime.time objects
    def _process_times(self, time_strings=[]):
        duration_indicators = [
            "MINUTES",
            "MIN",
            "MINS",
            "M",
            "HOURS",
            "HRS",
            "HRS",
            "H",
            "SECOND",
            "SECONDS",
            "SEC",
            "SECS",
        ]
        formatted = []
        discarded = []  # likely durations. Not needed, but grab for possible future dev
        for time in time_strings:
            if any(i in time.upper().split() for i in duration_indicators):
                discarded.append(time)
            else:
                try:
                    # remove common qualifiers
                    time = re.sub(r"approximately*|approx*|around*", r"", time).strip()
                    # convert synonyms
                    if time.upper() in ["MIDNIGHT", "MID NIGHT", "00:00"]:
                        formatted.append(
                            datetime.time(0, 0)
                        )  # add directly, as "00:00" not accepted later, due to dateutil bug
                    elif time.upper() in ["NOON"]:
                        time = "12:00"
                    # do some light string operations (regex) to detect semantic equivalences
                    time = re.sub(r"(\d{1,2})\.{1}(\d{2})(\D*)$", r"\1:\2\3", time)
                    time = re.sub(r"half past (\d{0,2}).*morning", r"\1:30am", time)
                    time = re.sub(r"half past (\d{0,2}).*afternoon", r"\1:30pm", time)
                    time = re.sub(r"half past (\d{0,2}).*night", r"\1:30pm", time)
                    time = re.sub(r"half past (\d{0,2}).*evening", r"\1:30pm", time)
                    time = re.sub(r"half\s{0,3}(\d{0,2}).*morning", r"\1:30am", time)
                    time = re.sub(r"(\d{0,4}).*morning", r"\1am", time)
                    time = re.sub(r"half\s{0,3}(\d{0,2}).*afternoon", r"\1:30pm", time)
                    time = re.sub(r"(\d{0,4}).*afternoon", r"\1pm", time)
                    time = re.sub(r"half\s{0,3}(\d{0,2}).*night", r"\1:30pm", time)
                    time = re.sub(r"(\d{0,4}).*night", r"\1pm", time)
                    time = re.sub(r"half\s{0,3}(\d{0,2}).*evening", r"\1:30pm", time)
                    time = re.sub(r"(\d{0,4}).*evening", r"\1pm", time)
                    time = re.sub(r"(\d{2})(\d{2})", r"\1:\2", time)
                    parsed = dateutil.parser.parse(time, fuzzy=True).time()
                    # do not add 0,0 as bag in dateutil erroneously defines some non-midnight to midnight
                    formatted.append(parsed) if parsed != datetime.time(0, 0) else None
                except ParserError:
                    discarded.append(time)
        return list(set(formatted)), discarded

    # process source URL
    def _process_source_url(self, url=""):
        # validate URL is formed correctly
        validator = URLValidator()
        try:
            validator(url)
            return url
        except ValidationError as e:
            logger.error(f"The URL was malformed - not saving.")
            return ""

    # process raw text account
    def _process_text(self, text=""):
        # do any string processing here, if required
        s = Scrubbers(text)
        return s.run_text_scrubbers()


class ProcessLocations:
    """
    Class to process locations. This is also accessible externally
    (outwith task scheduler processes). Includes geocode and
    formatting ready for DB insertion.
    """

    def __new__(cls, data=[], geocode=False):
        """
        incoming data (assigned to self._data), in form:
            ["City, State, Country", "City2, ...] when geocode = True
            ["City, State (longitude, latitude)", "City2, ...] when geocode = False
        """
        obj = super().__new__(cls)
        obj._data = data
        obj._geocode = geocode
        return obj._process()

    def _process(self):
        """
        Function to initiate the processing functions.
        Returns in the form [{"place_name": "place name string", "coordinates": Point(longitude, latitude)}]
        """
        processed = []
        for loc in self._data:
            if self._geocode:
                # remove existing coordinates from string in event record is being re-geocoded
                loc = re.sub(r"[(].*[)]", "", loc)
                # scrub location
                s = Scrubbers(loc)
                loc = s.run_place_scrubbers()
                try:
                    geolocator = Nominatim(user_agent="UAP_Database")
                    location = geolocator.geocode(loc)
                    processed.append(
                        {
                            "place_name": loc,
                            "coordinates": Point(location.longitude, location.latitude),
                        }
                    )
                except Exception as e:
                    logger.warning(
                        f"The token '{loc}' was not geocoded as it was unrecognised location, or an incorrect NER extraction."
                    )
                    processed.append(
                        {"place_name": loc, "coordinates": Point(0.0, 0.0)}
                    )
            else:
                # extract coordinates from string
                coordinates = re.findall("\(+(.*?)\)", loc)
                coordinates = [float(c.strip()) for c in coordinates[0].split(",")]
                coordinates = Point(coordinates[0], coordinates[1])
                # remove coordinates from string, leaving place name
                place_name = re.sub(r"[(].*[)]", "", loc)
                # scrub & append to processed
                s = Scrubbers(place_name)
                place_name = s.run_place_scrubbers()
                processed.append({"place_name": place_name, "coordinates": coordinates})
        return processed


class Scrubbers:
    """
    Class that provides the functions to clean and
    standardise the data
    """

    def __init__(self, input):
        self.input = input

    # runs set of functions to clean & standardise unstructured text field input
    def run_text_scrubbers(self):
        self._strip_quotes()
        self._remove_only_single_char()
        self._remove_whitespace()
        return self.input

    # runs set of functions to apply base cleaning & standardisation to any input text
    def run_base_scrubbers(self):
        self._remove_whitespace()
        self._capitalize()
        self._remove_nonalphanumeric()
        self._remove_only_single_char()
        return self.input

    # runs set of functions to clean & standardise place text (from LOC, GPE & PLACE fields)
    def run_place_scrubbers(self):
        self._remove_whitespace()
        self._capitalize()
        self._remove_nonalphanumeric(keep_commas=True)
        self._remove_only_single_char()
        return self.input

    # runs set of functions to clean & standardise colours
    def run_color_scrubbers(self):
        self.run_base_scrubbers()
        self._standardise_color()
        return self.input

    # runs functions to clean & standardise observation types
    def run_type_scrubbers(self):
        self.run_base_scrubbers()
        self._standardise_light()
        self._standardise_tictac()
        self._standardise_orb()
        self._standardise_fireball()
        self._standardise_triangle()
        self._standardise_rectangle()
        self._standardise_disk()
        self._standardise_circle()
        self._standardise_cigar()
        self._standardise_misc()
        self._remove_whitespace()
        return self.input

    # function to standardise colours
    def _standardise_color(self):
        extended_endings = ["ISH", "EY", "Y"]
        filtered = filter(
            lambda c: c in ColorFactory(endings=extended_endings), self.input.split()
        )
        self.input = " ".join(filtered)

    # function to remove the appended word "shaped"
    def _remove_shaped(self):
        self.input = re.sub(re.sub(r"\bSHAPED.*\b", "", self.input))

    # function to remote whitespace leading/trailing whitespace
    def _remove_whitespace(self):
        self.input = self.input.strip()

    # function to capitalize
    def _capitalize(self):
        self.input = self.input.upper()

    # function to remove non-alphanumeric characters (preserve whitespace, replace with space)
    def _remove_nonalphanumeric(self, keep_commas=False):
        if keep_commas:
            self.input = re.sub(r"[^\w\s,]", " ", self.input)
        else:
            self.input = re.sub(r"[^\w\s]", " ", self.input)

    # function to remove strings with single char
    def _remove_only_single_char(self):
        self.input = "" if len(self.input) <= 1 else self.input

    # function to strip quotation marks from beginning & end of string
    def _strip_quotes(self):
        self.input = self.input.strip('"')

    # function to change standardise 'light'
    def _standardise_light(self):
        self.input = re.sub(r"\b.*LIGHT.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\bDOT.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\bSTAR.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\bFLASH.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\b.*STREAK\b", "LIGHT", self.input)
        self.input = re.sub(r"\b.*GLOW.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\b.*PIN\s*PRICK.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\b.*STROBE.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\b.*TWINKLE.*\b", "LIGHT", self.input)
        self.input = re.sub(r"\bSATELLITE.*\b", "LIGHT", self.input)

    # function to change standardise 'fireball'
    def _standardise_fireball(self):
        self.input = re.sub(r"\b.*FIREBALL.*\b", "FIREBALL", self.input)

    # function to change standardise 'orb' (includes 'round').
    def _standardise_orb(self):
        self.input = re.sub(r"\b.*\s*ORB.*\b", "ORB", self.input)
        self.input = re.sub(r"\b.*ROUND\s*ORB.*\b", "ORB", self.input)
        self.input = re.sub(r"\bROUND\b", "ORB", self.input)
        self.input = re.sub(r"\bBALL.*\b", "ORB", self.input)

    # function to change standardise 'tic tac'.
    def _standardise_tictac(self):
        self.input = re.sub(r"\b.*TICT.*\b", "TIC TAC", self.input)
        self.input = re.sub(r"\b.*TIKT.*\b", "TIC TAC", self.input)
        self.input = re.sub(r"\b.*TIC T.*\b", "TIC TAC", self.input)

    # function to change standardise variations of 'triangle'.
    def _standardise_triangle(self):
        self.input = re.sub(r"\b.*RIANG.*\b", "TRIANGLE", self.input)

    # function to change standardise variations of 'rectangle'.
    def _standardise_rectangle(self):
        self.input = re.sub(r"\b.*RECTANG.*\b", "RECTANGLE", self.input)

    # function to change standardise variations of 'disk'.
    def _standardise_disk(self):
        self.input = re.sub(r"\b.*DISC.*\b", "DISK", self.input)
        self.input = re.sub(r"\b.*DISK.*\b", "DISK", self.input)
        self.input = re.sub(r"\b.*SAUCER.*\b", "DISK", self.input)

    # function to change standardise variations of 'circle'.
    def _standardise_circle(self):
        self.input = re.sub(r"\bCIRC.*\b", "CIRCLE", self.input)

    # function to change standardise variations of 'cigar'.
    def _standardise_cigar(self):
        self.input = re.sub(r"\bCIGAR.*\b", "CIGAR", self.input)

    # function to change standardise miscellaneous misfits'.
    def _standardise_misc(self):
        self.input = re.sub(r"\bUNKNOWN\b", "OTHER", self.input)
        self.input = re.sub(r"\bOBJECT.*\b", "OTHER", self.input)
        self.input = re.sub(r"\bUFO.*\b", "OTHER", self.input)
