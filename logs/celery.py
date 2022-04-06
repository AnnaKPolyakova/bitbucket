import os

from celery import Celery
from celery.schedules import crontab

from config.settings import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.SETTINGS_FOR_CELERY)

app = Celery("logs")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'logs.tasks.parsing_logs_task',
        'schedule': 30.0
        # 'schedule': crontab(seconds='*/10'),
    },
}

