from django.apps import AppConfig


class RestAPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statesngapps.apis.restapi'
    models_module = None
