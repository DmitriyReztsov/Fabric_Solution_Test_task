from django.contrib import admin

from .models import MailingList, Message


@admin.register(MailingList)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "started_on",
        "text",
        "filtering",
        "stop_mailing_by",
    )


@admin.register(Message)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "delivery_status", "created_on", "client_id")
