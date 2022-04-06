from .base import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = True

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': "localhost",
        'PORT': os.environ.get('DB_PORT'),
    }
}

REDIS_HOST = "0.0.0.0:"
REDIS_PORT = "6379"
CELERY_BROKER_URL = "redis://" + REDIS_HOST + REDIS_PORT + "/0"
CELERY_RESULT_BACKEND = "redis://" + REDIS_HOST + REDIS_PORT + "/0"