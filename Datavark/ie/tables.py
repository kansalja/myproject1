# tutorial/tables.py
import django_tables2 as tables
from django_q.models import Schedule, Task
from django.utils.html import format_html


class ScheduleTable(tables.Table):
    """
    Class to define the table to display
    currently scheduled tasks
    """

    class Meta:
        model = Schedule
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "schedule_type", "next_run")


class ResultsTable(tables.Table):
    """
    Class to define the table to display
    task execution results
    """

    class Meta:
        model = Task
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "group", "started", "stopped", "success", "result")
        order_by = "-stopped"

    def render_result(self, value, record):
        return (
            value[0:99] + "..."
            if len(value) > 102
            else value
            if record["success"]
            else format_html(
                f"Error acquiring data. See more in the <a href='/admin/django_q/failure/{record['id']}'>admin dashboard.</a>"
            )
        )
