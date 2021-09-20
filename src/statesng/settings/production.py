import os

from .base import *

SECRET_KEY = os.environ.get('STATESNG_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['statesng.com.ng', 'www.statesng.com.ng']

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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True
