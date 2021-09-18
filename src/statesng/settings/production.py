import os

from .base import *

SECRET_KEY = os.environ.get('STATESNG_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [os.environ.get('STATESNG_HOST')]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('STATESNG_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('STATESNG_DB_NAME', 'statesng_db'),
        'USER': os.environ.get('STATESNG_DB_USER', 'statesng_user'),
        'PASSWORD': os.environ.get('STATESNG_DB_PASSWORD', 'statesng_password'),
        'HOST': os.environ.get('STATESNG_DB_HOST', 'localhost'),
        'PORT': os.environ.get('STATESNG_DB_PORT', '5432')
    }
}
