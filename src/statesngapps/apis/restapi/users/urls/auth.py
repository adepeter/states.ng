from django.urls import path

from ..apiviews.auth import LoginAPIView

app_name = 'auth'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
]
