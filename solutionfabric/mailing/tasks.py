import os
from datetime import datetime, timedelta, timezone

import requests
from celery import Celery, shared_task
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solutionfabric.settings")

app = Celery("tasks", backend="rpc://", broker="pyamqp://")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


def preprocess_clients_list(mailing_list_id):
    from clients.models import Client

    from .models import MailingList, Message

    mailing_list = MailingList.objects.get(id=mailing_list_id)
    clients = Client.objects.filter(**mailing_list.filtering)

    data_to_send = {}
    for client in clients:
        message = Message(mailing_id=mailing_list, client_id=client)
        message.save()
        data_to_send[message.id] = {
            "id": int(client.id),
            "text": mailing_list.text,
            "phone": int(client.phone_number),
        }
    return data_to_send


def set_message_delivery_status(message_id, status_code):
    from .models import DeliveryStatus, Message

    message = Message.objects.get(id=message_id)
    if status_code == 200:
        message.delivery_status = DeliveryStatus.SENT
    else:
        message.delivery_status = DeliveryStatus.DELIVERY_ERROR
    message.save(update_fields=["delivery_status"])


@shared_task()
def perform_sending_mailing_list(mailing_list_id):
    json_datas = preprocess_clients_list(mailing_list_id)

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {settings.PROBE_TOKEN}",
    }

    for msg_id, json_data in json_datas.items():
        response = requests.post(
            f"{settings.PROBE_URL}/{msg_id}", headers=headers, json=json_data
        )
        set_message_delivery_status(msg_id, response.status_code)
    return None


def send_mailing_list(mailing_list):
    time_delay = mailing_list.started_on - datetime.now(timezone.utc)
    time_delay = time_delay.total_seconds() if time_delay.total_seconds() > 0 else 0
    time_in_future = datetime.now() + timedelta(seconds=time_delay)
    perform_sending_mailing_list.apply_async((mailing_list.id,), eta=time_in_future)
