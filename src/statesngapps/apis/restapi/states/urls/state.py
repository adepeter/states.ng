from django.urls import path, include

from ..apiviews.state import ListStatesAPIView, RetrieveStateAPIView

app_name = 'state'

urlpatterns = [
    path('', ListStatesAPIView.as_view(), name='list_states'),
    path('<str:state>/', include([
        path('', RetrieveStateAPIView.as_view(), name='retrieve_state'),
    ]))
]
