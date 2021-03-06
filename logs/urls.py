from django.urls import include, path
from rest_framework.routers import DefaultRouter

from logs.views import LogListView

router = DefaultRouter()
router.register(r"logs", LogListView, basename="logs")

clients_urls = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("v1/", include(clients_urls)),
]
