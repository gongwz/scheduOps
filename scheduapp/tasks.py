from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(120)
    return x + y

@shared_task
def mul(x, y):
    return x * y




