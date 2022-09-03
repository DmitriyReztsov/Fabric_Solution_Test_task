import pytz
from django.core.validators import RegexValidator
from django.db import models

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Client(models.Model):
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r"^1?[7]\d{10}$")], max_length=11
    )
    tag = models.SlugField()
    client_timezone = models.CharField(max_length=32, choices=TIMEZONES, default="UTC")
    operator_code = models.CharField(max_length=3, null=True)
