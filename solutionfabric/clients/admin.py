from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "operator_code",
        "tag",
        "client_timezone",
    )
