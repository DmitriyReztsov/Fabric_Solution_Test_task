from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MailingList, Message, DeliveryStatus
from .serializers import MailingListSerializer, MessageSerializer


@api_view(["GET"])
def general_mailing_stat(request):
    queryset = MailingList.objects.all().prefetch_related("sent_message")
    stat_dict = {}
    for mailing in queryset:
        messages = {}
        for status in DeliveryStatus:
            messages[status] = mailing.sent_message.filter(delivery_status=status).count()
        stat_dict[mailing.id] = messages
    return Response(data=stat_dict)


@api_view(["GET"])
def retrieval_mailing_stat(request, id=None):
    mailing_list = MailingList.objects.filter(id=id).prefetch_related("sent_message")
    if mailing_list:
        message = mailing_list.first().sent_message.all()
        data = MessageSerializer(message, many=True).data
        return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class MailingViewSet(viewsets.ModelViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer
