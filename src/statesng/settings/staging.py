from .base import *

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'statesng_db',
        'USER': 'statesng_user',
        'PASSWORD': 'statesng_password',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}
