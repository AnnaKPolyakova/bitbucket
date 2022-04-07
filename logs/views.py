from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from logs.filters import LogFilter
from logs.models import Log
from logs.serializers import LogSerializer


class LogListView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_class = LogFilter
    permission_classes = (IsAuthenticated,)
