from .base import *

SECRET_KEY = "django-insecure-f_ir^=iqz^96lc9)n=iw763#s1(m7ujc8awz8l_6937htytm_"

DEBUG = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


REDIS_HOST = "0.0.0.0:"
REDIS_PORT = "6379"
CELERY_BROKER_URL = "redis://" + REDIS_HOST + REDIS_PORT + "/0"
CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + REDIS_PORT + "/0"