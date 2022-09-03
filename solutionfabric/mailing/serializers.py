from pyexpat import model
from rest_framework import serializers

from .models import MailingList, Message
from .tasks import send_mailing_list


class MailingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = [
            "id",
            "started_on",
            "text",
            "filtering",
            "stop_mailing_by",
        ]

    def create(self, validated_data):
        mailing_list = super().create(validated_data)
        send_mailing_list(mailing_list)
        return mailing_list


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "id",
            "created_on",
            "delivery_status",
            "mailing_id",
            "client_id",
        ]
