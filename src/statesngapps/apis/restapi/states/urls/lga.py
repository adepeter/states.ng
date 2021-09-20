from django.urls import path

from ..apiviews.lga import ListLGAsAPIView, SearchLGAAPIView

app_name = 'lgas'

urlpatterns = [
    path('', ListLGAsAPIView.as_view(), name='list_lgas'),
    path('search/', SearchLGAAPIView.as_view(), name='search_lgas'),
]
