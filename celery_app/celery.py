from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')   # see https://github.com/celery/celery/issues/4081

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_app.settings')

app = Celery('celery_app.celery', backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# See http://docs.celeryproject.org/en/latest/userguide/routing.html
app.conf.task_default_queue = settings.CELERY_TASK_DEFAULT_QUEUE
app.conf.task_default_exchange = settings.CELERY_TASK_DEFAULT_EXCHANGE
app.conf.task_default_routing_key = settings.CELERY_TASK_DEFAULT_ROUTING_KEY


app.conf.beat_schedule = {
    'test_scheduling_tasks': {  # This task is only for test propose
        'task': 'celery_app.task.test_scheduling_tasks',
        'schedule': crontab(minute=0, hour=0),  # Run every day at 00:00
        'options': {'exchange': settings.CELERY_TASK_DEFAULT_EXCHANGE}
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
