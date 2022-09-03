from enum import Enum

from django.db import models


class DeliveryStatus(str, Enum):
    DRAFT = "draft"
    SENT = "sent"
    DELIVERY_ERROR = "delivery_error"


STATUS_CHOICES = [(choice.value, choice.value) for choice in DeliveryStatus]


class Message(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True, help_text="When it was created [autogen]"
    )
    delivery_status = models.CharField(
        choices=STATUS_CHOICES, max_length=64, default=DeliveryStatus.DRAFT
    )
    mailing_id = models.ForeignKey(
        "mailing.MailingList",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sent_message",
    )
    client_id = models.ForeignKey(
        "clients.Client",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sent_message",
    )


class MailingList(models.Model):
    started_on = models.DateTimeField(help_text="When delivery should start")
    text = models.CharField(null=True, blank=True, max_length=90)
    filtering = models.JSONField(default=dict)
    stop_mailing_by = models.DateTimeField(
        help_text="By which time delivery should stop"
    )
