from .staging import *

SECRET_KEY = os.environ.get('STATESNG_SECRET_KEY')

# DEBUG = False

INSTALLED_APPS += [
    'django_hosts',
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('STATESNG_DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('STATESNG_DB_NAME', 'statesng_db'),
        'USER': os.environ.get('STATESNG_DB_USER', 'statesng_user'),
        'PASSWORD': os.environ.get('STATESNG_DB_PASSWORD', 'statesng_password'),
        'HOST': os.environ.get('STATESNG_DB_HOST', 'localhost'),
        'PORT': os.environ.get('STATESNG_DB_PORT', 5432)
    }
}


# Caching
# https://docs.djangoproject.com/en/3.2/topics/cache/#setting-up-the-cache

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True

ALLOWED_HOSTS = ['google.com', 'api.google.com', 'www.google.com']

