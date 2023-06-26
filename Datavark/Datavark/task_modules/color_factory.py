class ColorFactory:
    """
    Class to create a list of acceptable values for
    colour names, including variations
    """

    def __new__(cls, endings=["ISH", "EY", "Y"]):
        obj = super().__new__(cls)
        obj.endings = endings
        return obj.get_colors()

    def get_colors(self):
        new_colors = []
        if self.endings:
            for ending in self.endings:  # add commonly used qualifiers
                for color in self._color_list:
                    new_colors.append(f"{color}{ending}")
        color_list_expanded = (
            self._color_list + new_colors if new_colors else self._color_list
        )
        color_list_expanded.sort()
        return color_list_expanded

    _color_list = [
        "GREY",
        "DARK GREY",
        "ABSOLUTE ZERO",
        "ACID GREEN",
        "AERO",
        "AERO BLUE",
        "AFRICAN VIOLET",
        "AIR FORCE BLUE",
        "AIR SUPERIORITY BLUE",
        "ALABAMA CRIMSON",
        "ALABASTER",
        "ALICE BLUE",
        "ALIEN ARMPIT",
        "ALIZARIN CRIMSON",
        "ALLOY ORANGE",
        "ALMOND",
        "AMARANTH",
        "AMARANTH DEEP PURPLE",
        "AMARANTH PINK",
        "AMARANTH PURPLE",
        "AMARANTH RED",
        "AMAZON",
        "AMAZONITE",
        "AMBER",
        "AMERICAN ROSE",
        "AMETHYST",
        "ANDROID GREEN",
        "ANTI-FLASH WHITE",
        "ANTIQUE BRASS",
        "ANTIQUE BRONZE",
        "ANTIQUE FUCHSIA",
        "ANTIQUE RUBY",
        "ANTIQUE WHITE",
        "AO",
        "APPLE GREEN",
        "APRICOT",
        "AQUA",
        "AQUAMARINE",
        "ARCTIC LIME",
        "ARMY GREEN",
        "ARSENIC",
        "ARTICHOKE",
        "ARYLIDE YELLOW",
        "ASH GREY",
        "ASPARAGUS",
        "ATOMIC TANGERINE",
        "AUBURN",
        "AUREOLIN",
        "AUROMETALSAURUS",
        "AVOCADO",
        "AWESOME",
        "AZTEC GOLD",
        "AZURE",
        "AZURE MIST",
        "AZUREISH WHITE",
        "B'DAZZLED BLUE",
        "BABY BLUE",
        "BABY BLUE EYES",
        "BABY PINK",
        "BABY POWDER",
        "BAKER-MILLER PINK",
        "BALL BLUE",
        "BANANA MANIA",
        "BANANA YELLOW",
        "BANGLADESH GREEN",
        "BARBIE PINK",
        "BARN RED",
        "BATTERY CHARGED BLUE",
        "BATTLESHIP GREY",
        "BAZAAR",
        "BEAU BLUE",
        "BEAVER",
        "BEGONIA",
        "BEIGE",
        "BIG DIP O’RUBY",
        "BIG FOOT FEET",
        "BISQUE",
        "BISTRE",
        "BISTRE BROWN",
        "BITTER LEMON",
        "BITTER LIME",
        "BITTERSWEET",
        "BITTERSWEET SHIMMER",
        "BLACK",
        "BLACK BEAN",
        "BLACK CORAL",
        "BLACK LEATHER JACKET",
        "BLACK OLIVE",
        "BLACK SHADOWS",
        "BLANCHED ALMOND",
        "BLAST-OFF BRONZE",
        "BLEU DE FRANCE",
        "BLIZZARD BLUE",
        "BLOND",
        "BLUE",
        "BLUE BELL",
        "BLUE BOLT",
        "BLUE JEANS",
        "BLUE LAGOON",
        "BLUE SAPPHIRE",
        "BLUE YONDER",
        "BLUE-GRAY",
        "BLUE-GREEN",
        "BLUE-MAGENTA VIOLET",
        "BLUE-VIOLET",
        "BLUEBERRY",
        "BLUEBONNET",
        "BLUSH",
        "BOLE",
        "BONDI BLUE",
        "BONE",
        "BOOGER BUSTER",
        "BOSTON UNIVERSITY RED",
        "BOTTLE GREEN",
        "BOYSENBERRY",
        "BRANDEIS BLUE",
        "BRASS",
        "BRICK RED",
        "BRIGHT CERULEAN",
        "BRIGHT GREEN",
        "BRIGHT LAVENDER",
        "BRIGHT LILAC",
        "BRIGHT MAROON",
        "BRIGHT NAVY BLUE",
        "BRIGHT PINK",
        "BRIGHT TURQUOISE",
        "BRIGHT UBE",
        "BRIGHT YELLOW",
        "BRILLIANT AZURE",
        "BRILLIANT LAVENDER",
        "BRILLIANT ROSE",
        "BRINK PINK",
        "BRITISH RACING GREEN",
        "BRONZE",
        "BRONZE YELLOW",
        "BROWN",
        "BROWN SUGAR",
        "BROWN YELLOW",
        "BROWN-NOSE",
        "BRUNSWICK GREEN",
        "BUBBLE GUM",
        "BUBBLES",
        "BUD GREEN",
        "BUFF",
        "BULGARIAN ROSE",
        "BURGUNDY",
        "BURLYWOOD",
        "BURNISHED BROWN",
        "BURNT ORANGE",
        "BURNT SIENNA",
        "BURNT UMBER",
        "BYZANTINE",
        "BYZANTIUM",
        "CADET",
        "CADET BLUE",
        "CADET GREY",
        "CADMIUM GREEN",
        "CADMIUM ORANGE",
        "CADMIUM RED",
        "CADMIUM YELLOW",
        "CAFÉ AU LAIT",
        "CAFÉ NOIR",
        "CAL POLY POMONA GREEN",
        "CAMBRIDGE BLUE",
        "CAMEL",
        "CAMEO PINK",
        "CAMOUFLAGE GREEN",
        "CANARY",
        "CANARY YELLOW",
        "CANDY APPLE RED",
        "CANDY PINK",
        "CAPRI",
        "CAPUT MORTUUM",
        "CARDINAL",
        "CARIBBEAN GREEN",
        "CARMINE",
        "CARMINE PINK",
        "CARMINE RED",
        "CARNATION PINK",
        "CARNELIAN",
        "CAROLINA BLUE",
        "CARROT ORANGE",
        "CASTLETON GREEN",
        "CATALINA BLUE",
        "CATAWBA",
        "CEDAR CHEST",
        "CEIL",
        "CELADON",
        "CELADON BLUE",
        "CELADON GREEN",
        "CELESTE",
        "CELESTIAL BLUE",
        "CERISE",
        "CERISE PINK",
        "CERULEAN",
        "CERULEAN BLUE",
        "CERULEAN FROST",
        "CG BLUE",
        "CG RED",
        "CHAMOISEE",
        "CHAMPAGNE",
        "CHAMPAGNE PINK",
        "CHARCOAL",
        "CHARLESTON GREEN",
        "CHARM PINK",
        "CHARTREUSE",
        "CHERRY",
        "CHERRY BLOSSOM PINK",
        "CHESTNUT",
        "CHINA PINK",
        "CHINA ROSE",
        "CHINESE RED",
        "CHINESE VIOLET",
        "CHLOROPHYLL GREEN",
        "CHOCOLATE",
        "CHROME YELLOW",
        "CINEREOUS",
        "CINNABAR",
        "CINNAMON SATIN",
        "CINNAMON[CITATION NEEDED]",
        "CITRINE",
        "CITRON",
        "CLARET",
        "CLASSIC ROSE",
        "COBALT BLUE",
        "COCOA BROWN",
        "COCONUT",
        "COFFEE",
        "COLUMBIA BLUE",
        "CONGO PINK",
        "COOL BLACK",
        "COOL GREY",
        "COPPER",
        "COPPER PENNY",
        "COPPER RED",
        "COPPER ROSE",
        "COQUELICOT",
        "CORAL",
        "CORAL PINK",
        "CORAL RED",
        "CORAL REEF",
        "CORDOVAN",
        "CORN",
        "CORNELL RED",
        "CORNFLOWER BLUE",
        "CORNSILK",
        "COSMIC COBALT",
        "COSMIC LATTE",
        "COTTON CANDY",
        "COYOTE BROWN",
        "CREAM",
        "CRIMSON",
        "CRIMSON GLORY",
        "CRIMSON RED",
        "CULTURED",
        "CYAN",
        "CYAN AZURE",
        "CYAN COBALT BLUE",
        "CYAN CORNFLOWER BLUE",
        "CYAN-BLUE AZURE",
        "CYBER GRAPE",
        "CYBER YELLOW",
        "CYCLAMEN",
        "DAFFODIL",
        "DANDELION",
        "DARK BLUE",
        "DARK BLUE-GRAY",
        "DARK BROWN",
        "DARK BROWN-TANGELO",
        "DARK BYZANTIUM",
        "DARK CANDY APPLE RED",
        "DARK CERULEAN",
        "DARK CHESTNUT",
        "DARK CORAL",
        "DARK CYAN",
        "DARK ELECTRIC BLUE",
        "DARK GOLDENROD",
        "DARK GRAY",
        "DARK GREEN",
        "DARK GUNMETAL",
        "DARK IMPERIAL BLUE",
        "DARK JUNGLE GREEN",
        "DARK KHAKI",
        "DARK LAVA",
        "DARK LAVENDER",
        "DARK LIVER",
        "DARK MAGENTA",
        "DARK MEDIUM GRAY",
        "DARK MIDNIGHT BLUE",
        "DARK MOSS GREEN",
        "DARK OLIVE GREEN",
        "DARK ORANGE",
        "DARK ORCHID",
        "DARK PASTEL BLUE",
        "DARK PASTEL GREEN",
        "DARK PASTEL PURPLE",
        "DARK PASTEL RED",
        "DARK PINK",
        "DARK POWDER BLUE",
        "DARK PUCE",
        "DARK PURPLE",
        "DARK RASPBERRY",
        "DARK RED",
        "DARK SALMON",
        "DARK SCARLET",
        "DARK SEA GREEN",
        "DARK SIENNA",
        "DARK SKY BLUE",
        "DARK SLATE BLUE",
        "DARK SLATE GRAY",
        "DARK SPRING GREEN",
        "DARK TAN",
        "DARK TANGERINE",
        "DARK TAUPE",
        "DARK TERRA COTTA",
        "DARK TURQUOISE",
        "DARK VANILLA",
        "DARK VIOLET",
        "DARK YELLOW",
        "DARTMOUTH GREEN",
        "DAVY'S GREY",
        "DEBIAN RED",
        "DEEP AQUAMARINE",
        "DEEP CARMINE",
        "DEEP CARMINE PINK",
        "DEEP CARROT ORANGE",
        "DEEP CERISE",
        "DEEP CHAMPAGNE",
        "DEEP CHESTNUT",
        "DEEP COFFEE",
        "DEEP FUCHSIA",
        "DEEP GREEN",
        "DEEP GREEN-CYAN TURQUOISE",
        "DEEP JUNGLE GREEN",
        "DEEP KOAMARU",
        "DEEP LEMON",
        "DEEP LILAC",
        "DEEP MAGENTA",
        "DEEP MAROON",
        "DEEP MAUVE",
        "DEEP MOSS GREEN",
        "DEEP PEACH",
        "DEEP PINK",
        "DEEP PUCE",
        "DEEP RED",
        "DEEP RUBY",
        "DEEP SAFFRON",
        "DEEP SKY BLUE",
        "DEEP SPACE SPARKLE",
        "DEEP SPRING BUD",
        "DEEP TAUPE",
        "DEEP TUSCAN RED",
        "DEEP VIOLET",
        "DEER",
        "DENIM",
        "DENIM BLUE",
        "DESATURATED CYAN",
        "DESERT",
        "DESERT SAND",
        "DESIRE",
        "DIAMOND",
        "DIM GRAY",
        "DINGY DUNGEON",
        "DIRT",
        "DODGER BLUE",
        "DOGWOOD ROSE",
        "DOLLAR BILL",
        "DOLPHIN GRAY",
        "DONKEY BROWN",
        "DRAB",
        "DUKE BLUE",
        "DUST STORM",
        "DUTCH WHITE",
        "EARTH YELLOW",
        "EBONY",
        "ECRU",
        "EERIE BLACK",
        "EGGPLANT",
        "EGGSHELL",
        "EGYPTIAN BLUE",
        "ELECTRIC BLUE",
        "ELECTRIC CRIMSON",
        "ELECTRIC CYAN",
        "ELECTRIC GREEN",
        "ELECTRIC INDIGO",
        "ELECTRIC LAVENDER",
        "ELECTRIC LIME",
        "ELECTRIC PURPLE",
        "ELECTRIC ULTRAMARINE",
        "ELECTRIC VIOLET",
        "ELECTRIC YELLOW",
        "EMERALD",
        "EMINENCE",
        "ENGLISH GREEN",
        "ENGLISH LAVENDER",
        "ENGLISH RED",
        "ENGLISH VERMILLION",
        "ENGLISH VIOLET",
        "ETON BLUE",
        "EUCALYPTUS",
        "FALLOW",
        "FALU RED",
        "FANDANGO",
        "FANDANGO PINK",
        "FASHION FUCHSIA",
        "FAWN",
        "FELDGRAU",
        "FELDSPAR",
        "FERN GREEN",
        "FERRARI RED",
        "FIELD DRAB",
        "FIERY ROSE",
        "FIRE ENGINE RED",
        "FIREBRICK",
        "FLAME",
        "FLAMINGO PINK",
        "FLATTERY",
        "FLAVESCENT",
        "FLAX",
        "FLIRT",
        "FLORAL WHITE",
        "FLUORESCENT ORANGE",
        "FLUORESCENT PINK",
        "FLUORESCENT YELLOW",
        "FOLLY",
        "FOREST GREEN",
        "FRENCH BEIGE",
        "FRENCH BISTRE",
        "FRENCH BLUE",
        "FRENCH FUCHSIA",
        "FRENCH LILAC",
        "FRENCH LIME",
        "FRENCH MAUVE",
        "FRENCH PINK",
        "FRENCH PLUM",
        "FRENCH PUCE",
        "FRENCH RASPBERRY",
        "FRENCH ROSE",
        "FRENCH SKY BLUE",
        "FRENCH VIOLET",
        "FRENCH WINE",
        "FRESH AIR",
        "FROSTBITE",
        "FUCHSIA",
        "FUCHSIA PINK",
        "FUCHSIA PURPLE",
        "FUCHSIA ROSE",
        "FULVOUS",
        "FUZZY WUZZY",
        "GAINSBORO",
        "GAMBOGE",
        "GAMBOGE ORANGE",
        "GARGOYLE GAS",
        "GENERIC VIRIDIAN",
        "GHOST WHITE",
        "GIANT'S CLUB",
        "GIANTS ORANGE",
        "GINGER",
        "GLAUCOUS",
        "GLITTER",
        "GLOSSY GRAPE",
        "GO GREEN",
        "GOLD",
        "GOLD FUSION",
        "GOLDEN BROWN",
        "GOLDEN POPPY",
        "GOLDEN YELLOW",
        "GOLDENROD",
        "GRANITE GRAY",
        "GRANNY SMITH APPLE",
        "GRAPE",
        "GRAY",
        "GRAY-ASPARAGUS",
        "GRAY-BLUE",
        "GREEN",
        "GREEN LIZARD",
        "GREEN SHEEN",
        "GREEN-BLUE",
        "GREEN-CYAN",
        "GREEN-YELLOW",
        "GRIZZLY",
        "GRULLO",
        "GUNMETAL",
        "GUPPIE GREEN",
        "HALAYÀ ÚBE",
        "HAN BLUE",
        "HAN PURPLE",
        "HANSA YELLOW",
        "HARLEQUIN",
        "HARLEQUIN GREEN",
        "HARVARD CRIMSON",
        "HARVEST GOLD",
        "HEART GOLD",
        "HEAT WAVE",
        "HEIDELBERG RED[2]",
        "HELIOTROPE",
        "HELIOTROPE GRAY",
        "HELIOTROPE MAGENTA",
        "HOLLYWOOD CERISE",
        "HONEYDEW",
        "HONOLULU BLUE",
        "HOOKER'S GREEN",
        "HOT MAGENTA",
        "HOT PINK",
        "HUNTER GREEN",
        "ICEBERG",
        "ICTERINE",
        "IGUANA GREEN",
        "ILLUMINATING EMERALD",
        "IMPERIAL",
        "IMPERIAL BLUE",
        "IMPERIAL PURPLE",
        "IMPERIAL RED",
        "INCHWORM",
        "INDEPENDENCE",
        "INDIA GREEN",
        "INDIAN RED",
        "INDIAN YELLOW",
        "INDIGO",
        "INDIGO DYE",
        "INFRA RED",
        "INTERDIMENSIONAL BLUE",
        "INTERNATIONAL KLEIN BLUE",
        "INTERNATIONAL ORANGE",
        "IRIS",
        "IRRESISTIBLE",
        "ISABELLINE",
        "ISLAMIC GREEN",
        "ITALIAN SKY BLUE",
        "IVORY",
        "JADE",
        "JAPANESE CARMINE",
        "JAPANESE INDIGO",
        "JAPANESE VIOLET",
        "JASMINE",
        "JASPER",
        "JAZZBERRY JAM",
        "JELLY BEAN",
        "JET",
        "JONQUIL",
        "JORDY BLUE",
        "JUNE BUD",
        "JUNGLE GREEN",
        "KELLY GREEN",
        "KENYAN COPPER",
        "KEPPEL",
        "KEY LIME",
        "KHAKI",
        "KIWI",
        "KOBE",
        "KOBI",
        "KOBICHA",
        "KOMBU GREEN",
        "KSU PURPLE",
        "KU CRIMSON",
        "LA SALLE GREEN",
        "LANGUID LAVENDER",
        "LAPIS LAZULI",
        "LASER LEMON",
        "LAUREL GREEN",
        "LAVA",
        "LAVENDER",
        "LAVENDER BLUE",
        "LAVENDER BLUSH",
        "LAVENDER GRAY",
        "LAVENDER INDIGO",
        "LAVENDER MAGENTA",
        "LAVENDER MIST",
        "LAVENDER PINK",
        "LAVENDER PURPLE",
        "LAVENDER ROSE",
        "LAWN GREEN",
        "LEMON",
        "LEMON CHIFFON",
        "LEMON CURRY",
        "LEMON GLACIER",
        "LEMON LIME",
        "LEMON MERINGUE",
        "LEMON YELLOW",
        "LIBERTY",
        "LICORICE",
        "LIGHT APRICOT",
        "LIGHT BLUE",
        "LIGHT BROWN",
        "LIGHT CARMINE PINK",
        "LIGHT COBALT BLUE",
        "LIGHT CORAL",
        "LIGHT CORNFLOWER BLUE",
        "LIGHT CRIMSON",
        "LIGHT CYAN",
        "LIGHT DEEP PINK",
        "LIGHT FRENCH BEIGE",
        "LIGHT FUCHSIA PINK",
        "LIGHT GOLDENROD YELLOW",
        "LIGHT GRAY",
        "LIGHT GRAYISH MAGENTA",
        "LIGHT GREEN",
        "LIGHT HOT PINK",
        "LIGHT KHAKI",
        "LIGHT MEDIUM ORCHID",
        "LIGHT MOSS GREEN",
        "LIGHT ORCHID",
        "LIGHT PASTEL PURPLE",
        "LIGHT PINK",
        "LIGHT RED OCHRE",
        "LIGHT SALMON",
        "LIGHT SALMON PINK",
        "LIGHT SEA GREEN",
        "LIGHT SKY BLUE",
        "LIGHT SLATE GRAY",
        "LIGHT STEEL BLUE",
        "LIGHT TAUPE",
        "LIGHT THULIAN PINK",
        "LIGHT YELLOW",
        "LILAC",
        "LILAC LUSTER",
        "LIME",
        "LIME GREEN",
        "LIMERICK",
        "LINCOLN GREEN",
        "LINEN",
        "LISERAN PURPLE",
        "LITTLE BOY BLUE",
        "LIVER",
        "LIVER CHESTNUT",
        "LIVID",
        "LOEENLOOK/VOMIT+INDOGO+LOPEN+GABRIEL",
        "LUMBER",
        "LUST",
        "MAASTRICHT BLUE",
        "MACARONI AND CHEESE",
        "MADDER LAKE",
        "MAGENTA",
        "MAGENTA HAZE",
        "MAGENTA-PINK",
        "MAGIC MINT",
        "MAGIC POTION",
        "MAGNOLIA",
        "MAHOGANY",
        "MAIZE",
        "MAJORELLE BLUE",
        "MALACHITE",
        "MANATEE",
        "MANDARIN",
        "MANGO TANGO",
        "MANTIS",
        "MARDI GRAS",
        "MARIGOLD",
        "MAROON",
        "MAUVE",
        "MAUVE TAUPE",
        "MAUVELOUS",
        "MAXIMUM BLUE",
        "MAXIMUM BLUE GREEN",
        "MAXIMUM BLUE PURPLE",
        "MAXIMUM GREEN",
        "MAXIMUM GREEN YELLOW",
        "MAXIMUM PURPLE",
        "MAXIMUM RED",
        "MAXIMUM RED PURPLE",
        "MAXIMUM YELLOW",
        "MAXIMUM YELLOW RED",
        "MAY GREEN",
        "MAYA BLUE",
        "MEAT BROWN",
        "MEDIUM AQUAMARINE",
        "MEDIUM BLUE",
        "MEDIUM CANDY APPLE RED",
        "MEDIUM CARMINE",
        "MEDIUM CHAMPAGNE",
        "MEDIUM ELECTRIC BLUE",
        "MEDIUM JUNGLE GREEN",
        "MEDIUM LAVENDER MAGENTA",
        "MEDIUM ORCHID",
        "MEDIUM PERSIAN BLUE",
        "MEDIUM PURPLE",
        "MEDIUM RED-VIOLET",
        "MEDIUM RUBY",
        "MEDIUM SEA GREEN",
        "MEDIUM SKY BLUE",
        "MEDIUM SLATE BLUE",
        "MEDIUM SPRING BUD",
        "MEDIUM SPRING GREEN",
        "MEDIUM TAUPE",
        "MEDIUM TURQUOISE",
        "MEDIUM TUSCAN RED",
        "MEDIUM VERMILION",
        "MEDIUM VIOLET-RED",
        "MELLOW APRICOT",
        "MELLOW YELLOW",
        "MELON",
        "METALLIC SEAWEED",
        "METALLIC SUNBURST",
        "MEXICAN PINK",
        "MIDDLE BLUE",
        "MIDDLE BLUE GREEN",
        "MIDDLE BLUE PURPLE",
        "MIDDLE GREEN",
        "MIDDLE GREEN YELLOW",
        "MIDDLE PURPLE",
        "MIDDLE RED",
        "MIDDLE RED PURPLE",
        "MIDDLE YELLOW",
        "MIDDLE YELLOW RED",
        "MIDNIGHT",
        "MIDNIGHT BLUE",
        "MIDNIGHT GREEN",
        "MIKADO YELLOW",
        "MILK",
        "MIMI PINK",
        "MINDARO",
        "MING",
        "MINION YELLOW",
        "MINT",
        "MINT CREAM",
        "MINT GREEN",
        "MISTY MOSS",
        "MISTY ROSE",
        "MOCCASIN",
        "MODE BEIGE",
        "MOONSTONE BLUE",
        "MORDANT RED 19",
        "MOSS GREEN",
        "MOUNTAIN MEADOW",
        "MOUNTBATTEN PINK",
        "MSU GREEN",
        "MUGHAL GREEN",
        "MULBERRY",
        "MUMMY'S TOMB",
        "MUSTARD",
        "MYRTLE GREEN",
        "MYSTIC",
        "MYSTIC MAROON",
        "NADESHIKO PINK",
        "NAPIER GREEN",
        "NAPLES YELLOW",
        "NAVAJO WHITE",
        "NAVY",
        "NAVY PURPLE",
        "NEON CARROT",
        "NEON FUCHSIA",
        "NEON GREEN",
        "NEW CAR",
        "NEW YORK PINK",
        "NICKEL",
        "NON-PHOTO BLUE",
        "NORTH TEXAS GREEN",
        "NYANZA",
        "OCEAN BLUE",
        "OCEAN BOAT BLUE",
        "OCEAN GREEN",
        "OCHRE",
        "OFFICE GREEN",
        "OGRE ODOR",
        "OLD BURGUNDY",
        "OLD GOLD",
        "OLD HELIOTROPE",
        "OLD LACE",
        "OLD LAVENDER",
        "OLD MAUVE",
        "OLD MOSS GREEN",
        "OLD ROSE",
        "OLD SILVER",
        "OLIVE",
        "OLIVE DRAB",
        "OLIVE DRAB #7",
        "OLIVINE",
        "ONYX",
        "OPERA MAUVE",
        "ORANGE",
        "ORANGE PEEL",
        "ORANGE SODA",
        "ORANGE-RED",
        "ORANGE-YELLOW",
        "ORCHID",
        "ORCHID PINK",
        "ORIOLES ORANGE",
        "OTTER BROWN",
        "OU CRIMSON RED",
        "OUTER SPACE",
        "OUTRAGEOUS ORANGE",
        "OXFORD BLUE",
        "PACIFIC BLUE",
        "PAKISTAN GREEN",
        "PALATINATE BLUE",
        "PALATINATE PURPLE",
        "PALE AQUA",
        "PALE BLUE",
        "PALE BROWN",
        "PALE CARMINE",
        "PALE CERULEAN",
        "PALE CHESTNUT",
        "PALE COPPER",
        "PALE CORNFLOWER BLUE",
        "PALE CYAN",
        "PALE GOLD",
        "PALE GOLDENROD",
        "PALE GREEN",
        "PALE LAVENDER",
        "PALE MAGENTA",
        "PALE MAGENTA-PINK",
        "PALE PINK",
        "PALE PLUM",
        "PALE RED-VIOLET",
        "PALE ROBIN EGG BLUE",
        "PALE SILVER",
        "PALE SPRING BUD",
        "PALE TAUPE",
        "PALE TURQUOISE",
        "PALE VIOLET",
        "PALE VIOLET-RED",
        "PALM LEAF",
        "PANSY PURPLE",
        "PAOLO VERONESE GREEN",
        "PAPAYA WHIP",
        "PARADISE PINK",
        "PARIS GREEN",
        "PARROT PINK",
        "PASTEL BLUE",
        "PASTEL BROWN",
        "PASTEL GRAY",
        "PASTEL GREEN",
        "PASTEL MAGENTA",
        "PASTEL ORANGE",
        "PASTEL PINK",
        "PASTEL PURPLE",
        "PASTEL RED",
        "PASTEL VIOLET",
        "PASTEL YELLOW",
        "PATRIARCH",
        "PAYNE'S GREY",
        "PEACH",
        "PEACH PUFF",
        "PEACH-ORANGE",
        "PEACH-YELLOW",
        "PEAR",
        "PEARL",
        "PEARL AQUA",
        "PEARLY PURPLE",
        "PERIDOT",
        "PERIWINKLE",
        "PERMANENT GERANIUM LAKE",
        "PERSIAN BLUE",
        "PERSIAN GREEN",
        "PERSIAN INDIGO",
        "PERSIAN ORANGE",
        "PERSIAN PINK",
        "PERSIAN PLUM",
        "PERSIAN RED",
        "PERSIAN ROSE",
        "PERSIMMON",
        "PERU",
        "PEWTER BLUE",
        "PHLOX",
        "PHTHALO BLUE",
        "PHTHALO GREEN",
        "PICTON BLUE",
        "PICTORIAL CARMINE",
        "PIGGY PINK",
        "PINE GREEN",
        "PINEAPPLE",
        "PINK",
        "PINK FLAMINGO",
        "PINK LACE",
        "PINK LAVENDER",
        "PINK PEARL",
        "PINK RASPBERRY",
        "PINK SHERBET",
        "PINK-ORANGE",
        "PISTACHIO",
        "PIXIE POWDER",
        "PLATINUM",
        "PLUM",
        "PLUMP PURPLE",
        "POLISHED PINE",
        "POMP AND POWER",
        "POPSTAR",
        "PORTLAND ORANGE",
        "POWDER BLUE",
        "PRINCESS PERFUME",
        "PRINCETON ORANGE",
        "PRUNE",
        "PRUSSIAN BLUE",
        "PSYCHEDELIC PURPLE",
        "PUCE",
        "PUCE RED",
        "PULLMAN BROWN",
        "PULLMAN GREEN",
        "PUMPKIN",
        "PURPLE",
        "PURPLE HEART",
        "PURPLE MOUNTAIN MAJESTY",
        "PURPLE NAVY",
        "PURPLE PIZZAZZ",
        "PURPLE PLUM",
        "PURPLE TAUPE",
        "PURPUREUS",
        "QUARTZ",
        "QUEEN BLUE",
        "QUEEN PINK",
        "QUICK SILVER",
        "QUINACRIDONE MAGENTA",
        "RACKLEY",
        "RADICAL RED",
        "RAISIN BLACK",
        "RAJAH",
        "RASPBERRY",
        "RASPBERRY GLACE",
        "RASPBERRY PINK",
        "RASPBERRY ROSE",
        "RAW SIENNA",
        "RAW UMBER",
        "RAZZLE DAZZLE ROSE",
        "RAZZMATAZZ",
        "RAZZMIC BERRY",
        "REBECCA PURPLE",
        "RED",
        "RED DEVIL",
        "RED SALSA",
        "RED-BROWN",
        "RED-ORANGE",
        "RED-PURPLE",
        "RED-VIOLET",
        "REDWOOD",
        "REGALIA",
        "REGISTRATION BLACK",
        "RESOLUTION BLUE",
        "RHYTHM",
        "RICH BLACK",
        "RICH BRILLIANT LAVENDER",
        "RICH CARMINE",
        "RICH ELECTRIC BLUE",
        "RICH LAVENDER",
        "RICH LILAC",
        "RICH MAROON",
        "RIFLE GREEN",
        "ROAST COFFEE",
        "ROBIN EGG BLUE",
        "ROCKET METALLIC",
        "ROMAN SILVER",
        "ROSE",
        "ROSE BONBON",
        "ROSE DUST",
        "ROSE EBONY",
        "ROSE GOLD",
        "ROSE MADDER",
        "ROSE PINK",
        "ROSE QUARTZ",
        "ROSE RED",
        "ROSE TAUPE",
        "ROSE VALE",
        "ROSEWOOD",
        "ROSSO CORSA",
        "ROSY BROWN",
        "ROYAL AZURE",
        "ROYAL BLUE",
        "ROYAL FUCHSIA",
        "ROYAL PURPLE",
        "ROYAL YELLOW",
        "RUBER",
        "RUBINE RED",
        "RUBY",
        "RUBY RED",
        "RUDDY",
        "RUDDY BROWN",
        "RUDDY PINK",
        "RUFOUS",
        "RUSSET",
        "RUSSIAN GREEN",
        "RUSSIAN VIOLET",
        "RUST",
        "RUSTY RED",
        "SACRAMENTO STATE GREEN",
        "SADDLE BROWN",
        "SAFETY ORANGE",
        "SAFETY YELLOW",
        "SAFFRON",
        "SAGE",
        "SALMON",
        "SALMON PINK",
        "SAND",
        "SAND DUNE",
        "SANDSTORM",
        "SANDY BROWN",
        "SANDY TAN",
        "SANDY TAUPE",
        "SANGRIA",
        "SAP GREEN",
        "SAPPHIRE",
        "SAPPHIRE BLUE",
        "SASQUATCH SOCKS",
        "SATIN SHEEN GOLD",
        "SCARLET",
        "SCHAUSS PINK",
        "SCHOOL BUS YELLOW",
        "SCREAMIN' GREEN",
        "SEA BLUE",
        "SEA FOAM GREEN",
        "SEA GREEN",
        "SEA SERPENT",
        "SEAL BROWN",
        "SEASHELL",
        "SELECTIVE YELLOW",
        "SEPIA",
        "SHADOW",
        "SHADOW BLUE",
        "SHAMPOO",
        "SHAMROCK GREEN",
        "SHEEN GREEN",
        "SHIMMERING BLUSH",
        "SHINY SHAMROCK",
        "SHOCKING PINK",
        "SIENNA",
        "SILVER",
        "SILVER CHALICE",
        "SILVER LAKE BLUE",
        "SILVER PINK",
        "SILVER SAND",
        "SINOPIA",
        "SIZZLING RED",
        "SIZZLING SUNRISE",
        "SKOBELOFF",
        "SKY BLUE",
        "SKY MAGENTA",
        "SLATE BLUE",
        "SLATE GRAY",
        "SLIMY GREEN",
        "SMALT",
        "SMASHED PUMPKIN",
        "SMITTEN",
        "SMOKE",
        "SMOKEY TOPAZ",
        "SMOKY BLACK",
        "SMOKY TOPAZ",
        "SNOW",
        "SOAP",
        "SOLID PINK",
        "SONIC SILVER",
        "SPACE CADET",
        "SPANISH BISTRE",
        "SPANISH BLUE",
        "SPANISH CARMINE",
        "SPANISH CRIMSON",
        "SPANISH GRAY",
        "SPANISH GREEN",
        "SPANISH ORANGE",
        "SPANISH PINK",
        "SPANISH RED",
        "SPANISH SKY BLUE",
        "SPANISH VIOLET",
        "SPANISH VIRIDIAN",
        "SPARTAN CRIMSON",
        "SPICY MIX",
        "SPIRO DISCO BALL",
        "SPRING BUD",
        "SPRING FROST",
        "SPRING GREEN",
        "ST. PATRICK'S BLUE",
        "STAR COMMAND BLUE",
        "STEEL BLUE",
        "STEEL PINK",
        "STEEL TEAL",
        "STIL DE GRAIN YELLOW",
        "STIZZA",
        "STORMCLOUD",
        "STRAW",
        "STRAWBERRY",
        "SUGAR PLUM",
        "SUNBURNT CYCLOPS",
        "SUNGLOW",
        "SUNNY",
        "SUNRAY",
        "SUNSET",
        "SUNSET ORANGE",
        "SUPER PINK",
        "SWEET BROWN",
        "TAN",
        "TANGELO",
        "TANGERINE",
        "TANGERINE YELLOW",
        "TANGO PINK",
        "TART ORANGE",
        "TAUPE",
        "TAUPE GRAY",
        "TEA GREEN",
        "TEA ROSE",
        "TEAL",
        "TEAL BLUE",
        "TEAL DEER",
        "TEAL GREEN",
        "TELEMAGENTA",
        "TENNÉ",
        "TERRA COTTA",
        "THISTLE",
        "THULIAN PINK",
        "TICKLE ME PINK",
        "TIFFANY BLUE",
        "TIGER'S EYE",
        "TIMBERWOLF",
        "TITANIUM YELLOW",
        "TOMATO",
        "TOOLBOX",
        "TOPAZ",
        "TRACTOR RED",
        "TROLLEY GREY",
        "TROPICAL RAIN FOREST",
        "TROPICAL VIOLET",
        "TRUE BLUE",
        "TUFTS BLUE",
        "TULIP",
        "TUMBLEWEED",
        "TURKISH ROSE",
        "TURQUOISE",
        "TURQUOISE BLUE",
        "TURQUOISE GREEN",
        "TURQUOISE SURF",
        "TURTLE GREEN",
        "TUSCAN",
        "TUSCAN BROWN",
        "TUSCAN RED",
        "TUSCAN TAN",
        "TUSCANY",
        "TWILIGHT LAVENDER",
        "TYRIAN PURPLE",
        "UA BLUE",
        "UA RED",
        "UBE",
        "UCLA BLUE",
        "UCLA GOLD",
        "UFO GREEN",
        "ULTRA PINK",
        "ULTRA RED",
        "ULTRAMARINE",
        "ULTRAMARINE BLUE",
        "UMBER",
        "UNBLEACHED SILK",
        "UNITED NATIONS BLUE",
        "UNIVERSITY OF CALIFORNIA GOLD",
        "UNIVERSITY OF TENNESSEE ORANGE",
        "UNMELLOW YELLOW",
        "UP FOREST GREEN",
        "UP MAROON",
        "UPSDELL RED",
        "UROBILIN",
        "USAFA BLUE",
        "USC CARDINAL",
        "USC GOLD",
        "UTAH CRIMSON",
        "VAN DYKE BROWN",
        "VANILLA",
        "VANILLA ICE",
        "VEGAS GOLD",
        "VENETIAN RED",
        "VERDIGRIS",
        "VERMILION",
        "VERONICA",
        "VERY LIGHT AZURE",
        "VERY LIGHT BLUE",
        "VERY LIGHT MALACHITE GREEN",
        "VERY LIGHT TANGELO",
        "VERY PALE ORANGE",
        "VERY PALE YELLOW",
        "VIOLET",
        "VIOLET-BLUE",
        "VIOLET-RED",
        "VIRIDIAN",
        "VIRIDIAN GREEN",
        "VISTA BLUE",
        "VIVID AMBER",
        "VIVID AUBURN",
        "VIVID BURGUNDY",
        "VIVID CERISE",
        "VIVID CERULEAN",
        "VIVID CRIMSON",
        "VIVID GAMBOGE",
        "VIVID LIME GREEN",
        "VIVID MALACHITE",
        "VIVID MULBERRY",
        "VIVID ORANGE",
        "VIVID ORANGE PEEL",
        "VIVID ORCHID",
        "VIVID RASPBERRY",
        "VIVID RED",
        "VIVID RED-TANGELO",
        "VIVID SKY BLUE",
        "VIVID TANGELO",
        "VIVID TANGERINE",
        "VIVID VERMILION",
        "VIVID VIOLET",
        "VIVID YELLOW",
        "VOLT",
        "WAGENINGEN GREEN",
        "WARM BLACK",
        "WATERSPOUT",
        "WELDON BLUE",
        "WENGE",
        "WHEAT",
        "WHITE",
        "WHITE SMOKE",
        "WILD BLUE YONDER",
        "WILD ORCHID",
        "WILD STRAWBERRY",
        "WILD WATERMELON",
        "WILLPOWER ORANGE",
        "WINDSOR TAN",
        "WINE",
        "WINE DREGS",
        "WINTER SKY",
        "WINTER WIZARD",
        "WINTERGREEN DREAM",
        "WISTERIA",
        "WOOD BROWN",
        "XANADU",
        "YALE BLUE",
        "YANKEES BLUE",
        "YELLOW",
        "YELLOW ORANGE",
        "YELLOW ROSE",
        "YELLOW SUNSHINE",
        "YELLOW-GREEN",
        "ZAFFRE",
        "ZINNWALDITE BROWN",
        "ZOMP",
    ]