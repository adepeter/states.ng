from django.apps import AppConfig


class GraphQLConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statesngapps.graphql'
    models_module = None
