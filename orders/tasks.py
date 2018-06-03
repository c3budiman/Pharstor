from celery.task.base import task
from django.core.mail import send_mail

from orders.models import Order


@task
def order_created(order_id):

    return True
