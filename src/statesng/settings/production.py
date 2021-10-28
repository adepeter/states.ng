from .staging import *

SECRET_KEY = os.environ.get('STATESNG_SECRET_KEY')
ALLOWED_HOST = os.environ.get('ROOT_DOMAIN_NAME', 'statesng.com.ng')


# DEBUG = False
# ALLOWED_HOSTS = [
#     '{domain}',
#     'www.{domain}',
#     'cpanel.{domain}',
#     'pages.{domain}',
#     'api.{domain}'.format(domain=ALLOWED_HOST)
# ]

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
        'PORT': os.environ.get('STATESNG_DB_PORT', '5432')
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

USE_X_FORWARDED_PORT = True
