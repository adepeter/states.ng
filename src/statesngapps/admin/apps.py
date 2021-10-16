from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statesngapps.admin'
    models_module = None
    verbose_name = 'Admin'
    label = 'statesng_admin'


class StatesNGAdminConfig(AdminConfig):
    default_site = 'statesng.admin.StatesNGAdminSite'
