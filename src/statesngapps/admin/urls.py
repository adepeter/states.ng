from django.urls import path

from .admin import admin_site

app_name = 'admin'

urlpatterns = [
    path('admins/', admin_site.urls),
]
