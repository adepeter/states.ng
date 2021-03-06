"""
WSGI config for statesng project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

deployment_environment = os.environ.get('DEPLOYMENT_ENVIRONMENT', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'statesng.settings.{deployment_environment}')

application = get_wsgi_application()
