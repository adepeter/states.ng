from django.urls import path

from ..views.contact import ContactUsView

app_name = 'contact'

urlpatterns = [
    path('', ContactUsView.as_view(), name='contact_us')
]
