from .base import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    # API apps
    'statesngapps.apis.graphql.apps.GraphQLConfig',
    'statesngapps.apis.restapi.apps.RestAPIConfig',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
