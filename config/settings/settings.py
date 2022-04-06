from .base import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    "default": {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': "db",
        'PORT': os.environ.get('DB_PORT'),
    }
}

REDIS_HOST = "redis:"
REDIS_PORT = "6379"
CELERY_BROKER_URL = "redis://" + REDIS_HOST + REDIS_PORT + "/0"
CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + REDIS_PORT + "/0"