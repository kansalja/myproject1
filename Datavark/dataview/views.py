from django.shortcuts import render, redirect
from django.views import View
from Datavark.da_settings import DA_SETTINGS as d_set
from django import template
from django.db.models import F
from django_tables2 import SingleTableMixin, LazyPaginator, RequestConfig
from .tables import ReportTable
from django.http import FileResponse, JsonResponse
from Datavark.task_modules import db
from Datavark.task_modules.postprocess import Scrubbers, ProcessLocations
import ie.models as data_models
import logging, random, os
import pandas as pd
import datetime

register = template.Library()
logger = logging.getLogger("django")


class GetData:
    """
    Class to get the data from the database
    """

    _report_model = data_models.Report

    def __new__(cls, id=None):
        obj = super().__new__(cls)
        obj._id = id
        return obj._get_data()

    def _get_data(self):
        # get one record, by ID
        if self._id:
            reports = self._report_model.objects.filter(id=self._id)
            reports = (
                reports.filter(record_junked=False)
                if d_set["exclude_junked"]
                else reports
            )
            reports = reports[0]
        else:
            # get all reports in database
            reports = self._report_model.objects.all()
            # filter out junked records if configured in settings
            reports = (
                reports.filter(record_junked=False)
                if d_set["exclude_junked"]
                else reports
            )
            # only return records with dates (if configured in settings)
            reports = (
                reports.filter(obs_dates__isnull=False)
                if d_set["exclude_no_date"]
                else reports
            )
            # only return records with times (if configured in settings)
            reports = (
                reports.filter(obs_times__isnull=False)
                if d_set["exclude_no_time"]
                else reports
            )
            # only return records with locations (if configured in settings)
            reports = (
                reports.filter(obs_locs__isnull=False)
                if d_set["exclude_no_loc"]
                else reports
            )
            # only return records with types (if configured in settings)
            reports = (
                reports.filter(obs_types__isnull=False)
                if d_set["exclude_no_type"]
                else reports
            )
            # only return records with colours (if configured in settings)
            reports = (
                reports.filter(obs_colors__isnull=False)
                if d_set["exclude_no_color"]
                else reports
            )
            # order by last modified, or order by obs_dates__date for observation date
            reports = reports.order_by(F("last_mod").desc(nulls_last=True))
            # ensure no duplicated (fix for Django 'bug' where filtering M2M fields returns duplicates)
            reports = reports.distinct()
        return reports


class ReportsView(SingleTableMixin, View):
    """
    Class to present all data to the user,
    in tabular format
    """

    _template_name = "dataview/reportsview.html"

    _report_table_class = ReportTable
    paginator_class = LazyPaginator

    # handle GET requests
    def get(self, *args, **kwargs):
        report_table = self._report_table_class(GetData())
        RequestConfig(
            self.request, paginate={"per_page": d_set["records_to_display_per_page"]}
        ).configure(report_table)
        _context = {
            "reports_table": report_table,
            "request": self.request,
        }
        return render(self.request, self._template_name, _context)


class DetailView(SingleTableMixin, View):
    """
    Class to present a single record to the user,
    & to enable modifying/deletion of that record
    """

    _template_name = "dataview/detailview.html"

    # define GET requests
    def get(self, *args, **kwargs):
        context = dict()
        report_id = kwargs.get("id", None)
        if report_id:
            try:
                report = GetData(id=report_id)
                context = {"report": report}
            except Exception as e:
                logger.error(f"Report ID {report_id} cannot be retrieved! {str(e)}")
                return redirect("dataview:reports-view")
        return render(self.request, self._template_name, context)

    # define POST requests
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            report_id = kwargs.get("id", None)
            data = self.request.POST
            if data:
                update_data = {"report_id": report_id}
                dates = data.getlist("date")
                newDates = data.getlist("newDate")
                times = data.getlist("time")
                newTimes = data.getlist("newTime")
                types = data.getlist("type")
                newTypes = data.getlist("newTypes")
                colors = data.getlist("color")
                newColors = data.getlist("newColors")
                locations = data.getlist("location")
                newLocations = data.getlist("newLocations")
                report_txt = data.getlist("report_txt")
                delete_record = data.get("delete_record")
                # if delete record
                if delete_record:
                    junked = db.JunkRecord(record_id=report_id)
                    return JsonResponse({"success": True}, status=200)
                # clear existing extracted data from record
                db.ClearRelations(record_id=report_id)
                if report_txt:
                    try:
                        update_data.update({"obs_txt": report_txt[0]})
                    except Exception as e:
                        logger.error(f"Adding report text failed: {e}")
                if dates or newDates:  # add dates
                    try:
                        update_data.update(
                            {
                                "obs_dates": [
                                    datetime.datetime.strptime(d, "%Y-%m-%d").date()
                                    for d in dates
                                ]
                                + (
                                    [
                                        datetime.datetime.strptime(d, "%Y-%m-%d").date()
                                        for d in newDates
                                    ]
                                    if newDates
                                    else []
                                )
                            }
                        )
                    except Exception as e:
                        logger.error(f"Adding date data failed: {e}")
                if times or newTimes:  # add times
                    try:
                        update_data.update(
                            {
                                "obs_times": [
                                    datetime.datetime.strptime(t, "%H:%M").time()
                                    for t in times
                                ]
                                + (
                                    [
                                        datetime.datetime.strptime(t, "%H:%M").time()
                                        for t in newTimes
                                    ]
                                    if newTimes
                                    else []
                                )
                            }
                        )
                    except Exception as e:
                        logger.error(f"Adding time data failed: {e}")
                if types or newTypes:  # add types
                    processed_types = []
                    if newTypes:
                        for t in newTypes[0].split(","):
                            s = Scrubbers(t)
                            t = s.run_base_scrubbers()
                            processed_types.append(t)
                    for t in types:
                        for t in t.split(","):
                            s = Scrubbers(t)
                            t = s.run_base_scrubbers()
                            processed_types.append(t)
                    update_data.update({"obs_types": processed_types})
                if colors or newColors:  # add colours
                    processed_colors = []
                    if newColors:
                        for c in newColors[0].split(","):
                            s = Scrubbers(c)
                            c = s.run_base_scrubbers()
                            processed_colors.append(c)
                    for c in colors:
                        for c in c.split(","):
                            s = Scrubbers(c)
                            c = s.run_base_scrubbers()
                            processed_colors.append(c)
                    update_data.update({"obs_colors": processed_colors})
                if locations or newLocations:  # add locations
                    processed_locs = (
                        []
                    )  # in format {"place_name": "example", "coordinates": Point(123,456)}
                    if newLocations:
                        # run geocoding & scrubbing, then append to processed
                        processed_locs += ProcessLocations(
                            [l.strip() for l in newLocations[0].split("/")],
                            geocode=True,
                        )
                    for l in locations:
                        processed_locs += ProcessLocations([l], geocode=True)
                    # update obs_locs
                    update_data.update({"obs_locs": processed_locs})
                # make call to update db here
                update_outcome = db.UpdateDB(update_data)
                logger.info(f"Update outcome: {update_outcome}")
                # return to UI
                return JsonResponse({"success": True}, status=200)
            else:
                return JsonResponse({"success": False}, status=400)
        return JsonResponse({"success": False}, status=400)


class DataExportView(View):
    """
    Class to exports the data upon user request, as CSV files
    """

    _template_name = "dataview/dataexportview.html"
    _export_path = d_set["csv_export_path"]
    _export_filename = d_set["csv_export_filename"]

    # handle GET requests
    def get(self, *args, **kwargs):
        random_sample = True if self.request.GET.get("random", "") == "true" else False
        source = self.request.GET.get("source", "")
        if self.request.GET.get("download", "false") == "true":
            try:
                self._export_records_csv(self.request, source, random_sample)
                response = FileResponse(
                    open(os.path.join(self._export_path, self._export_filename), "rb")
                )
                response["Content-Disposition"] = (
                    "inline; filename=" + self._export_filename
                )
                return response
            except Exception as e:
                logger.error(f"Data export failed: {str(e)}")
                status = f"Export failed: {str(e)}"
                return render(self.request, self._template_name, {"status": status})
        else:
            return render(
                self.request,
                self._template_name,
                {"record_num": d_set["total_export_records"]},
            )

    def _export_records_csv(self, request, source, random_sample):
        # get record list for sources
        records = GetData()
        records_list = (
            # get records from the specified source
            list(records.filter(source_name=source.upper()))
            if source
            # or, get all records if no source specified
            else list(records)
        )
        # either export random selection, or all, depending on button user clicked
        records = (
            random.sample(records_list, d_set["total_export_records"])
            if random_sample
            else records_list
        )
        # create data including from related tables
        data = []
        for report in records:
            data.append(
                {
                    "id": report.id,
                    "record_created": report.record_created,
                    "last_mod": report.last_mod,
                    "source_name": report.source_name,
                    "source_url": report.source_url,
                    "obs_txt": report.obs_txt,
                    "obs_types": [t.type for t in report.obs_types.all()],
                    "obs_colors": [c.color for c in report.obs_colors.all()],
                    "obs_locs": [
                        (
                            l.place_name,
                            {"longitude": l.coordinates.x, "latitude": l.coordinates.y},
                        )
                        for l in report.obs_locs.all()
                    ],
                    "obs_dates": [d.date for d in report.obs_dates.all()],
                    "obs_times": [t.time for t in report.obs_times.all()],
                }
            )
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(self._export_path, self._export_filename))
