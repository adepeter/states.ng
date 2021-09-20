from django.urls import path, re_path, include

from ..apiviews.state import ListStatesAPIView, ListCitiesInStateAPIView, ListLGAsForStateAPIView, RetrieveStateAPIView

app_name = 'state'

urlpatterns = [
    path('', ListStatesAPIView.as_view(), name='list_states'),
    path('<str:state>/', include([
        path('', RetrieveStateAPIView.as_view(), name='retrieve_state'),
        path('cities/', ListCitiesInStateAPIView.as_view(), name='list_cities_in_state'),
        path('lgas/', ListLGAsForStateAPIView.as_view(), name='list_state_lgas'),
    ]))
]
