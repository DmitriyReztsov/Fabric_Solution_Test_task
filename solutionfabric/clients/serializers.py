from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "phone_number",
            "operator_code",
            "tag",
            "client_timezone",
        ]

    def validate(self, data):
        phone_number = data.get("phone_number")
        validated_data = super().validate(data)
        validated_data["operator_code"] = phone_number[1:4]
        return validated_data
