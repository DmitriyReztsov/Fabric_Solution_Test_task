from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import ClientViewSet

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
