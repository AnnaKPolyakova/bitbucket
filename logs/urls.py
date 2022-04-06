from django.urls import include, path
from rest_framework.routers import DefaultRouter

from logs.views import LogViewSet

router = DefaultRouter()
router.register(r"logs", LogViewSet, basename="logs")

clients_urls = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("v1/", include(clients_urls)),
]
