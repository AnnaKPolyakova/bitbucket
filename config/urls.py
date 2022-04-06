from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

DEBUG = settings.DEBUG


apps_patterns = [
    path("", include("logs.urls")),
]


api_schema_patterns = [
    path("", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(apps_patterns)),
    path(
        "api/v1/schema/",
        include(api_schema_patterns),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
