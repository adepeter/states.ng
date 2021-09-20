from django.urls import path, include

app_name = 'states'

urlpatterns = [
    path('states/', include('statesngapps.apis.restapi.states.urls.state', namespace='state')),
    path('lgas/', include('statesngapps.apis.restapi.states.urls.lga', namespace='lga')),
]
