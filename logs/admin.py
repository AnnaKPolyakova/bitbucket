from django.contrib import admin
from django.contrib.admin import register
from django_admin_listfilter_dropdown.filters import DropdownFilter
from rangefilter.filters import DateTimeRangeFilter

from logs.models import Log


@register(Log)
class LogAdmin(admin.ModelAdmin):

    list_display = ("host", "request_time", "request_line", "final_status")
    list_filter = (
        ("host", DropdownFilter),
        ("request_time", DateTimeRangeFilter),
    )
