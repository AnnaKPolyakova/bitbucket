from django_filters import FilterSet, filters

from logs.models import Log


class LogFilter(FilterSet):
    start_request_time = filters.DateTimeFilter(
        field_name="request_time", lookup_expr="gte"
    )
    end_request_time = filters.DateTimeFilter(
        field_name="request_time",lookup_expr="lte"
    )

    class Meta:
        model = Log
        fields = [
            "start_request_time",
            "end_request_time",
            "host",
        ]
