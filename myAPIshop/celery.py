"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""
from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
from myAPIshop import settings
import logging



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAPIshop.settings')

app = Celery("myAPIshop")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from django.apps import apps


@app.task
def select_brand():
    Product = apps.get_model("myshop.Product")
    products = Product.objects.all()
    total = 0
    for product in products:
        if 'ATN' in product.article:
            product.collection_name_id = 1
            product.brend_name_id = 1
            product.save()
            logging.info(f'{product.id} DONE')
            total += 1
    logging.info(f"DONE {total}")


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'myshop.tasks.group_by_color',
        'schedule': 10000000.0
    },
    'clear-basket-one-time-a-day': {
        'task': 'myshop.tasks.clear_basket',
        'schedule': crontab(minute=0, hour=0)
    },
}
