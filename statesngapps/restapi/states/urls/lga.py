from django.urls import path

from ..apiviews.lga import ListLGAsAPIView

app_name = 'lgas'

urlpatterns = [
    path('', ListLGAsAPIView.as_view(), name='list_lgas')
]
