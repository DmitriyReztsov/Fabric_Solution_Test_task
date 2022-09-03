from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

schema_view = get_schema_view(
    openapi.Info(
        title="Mailing Service API",
        default_version="v1",
        description="API documentation for test task from Solution Fabric",
        contact=openapi.Contact(email="rezcov_d@mail.ru"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

urlpatterns = [
    path("mailing/", include("mailing.urls")),
    path("clients/", include("clients.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
