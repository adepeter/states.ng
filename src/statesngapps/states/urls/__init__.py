from django.urls import path

from .. import views

app_name = 'states'

urlpatterns = [
    path('', views.home, name='home')
]
