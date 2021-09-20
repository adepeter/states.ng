from django.apps import AppConfig


class GraphQLConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statesngapps.apis.graphql'
    models_module = None
