from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import MailingViewSet, general_mailing_stat, retrieval_mailing_stat

router = routers.DefaultRouter()
router.register(r"mailings", MailingViewSet, basename="mailing")
urlpatterns = [
    path("statistic/", general_mailing_stat),
    path("statistic/<int:id>/", retrieval_mailing_stat),
    path("", include(router.urls)),
]
