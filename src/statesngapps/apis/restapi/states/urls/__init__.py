from django.urls import path, re_path, include

app_name = 'states'

urlpatterns = [
    path('states/', include('statesngapps.api.restapi.states.urls.state', namespace='state')),
    path('lgas/', include('statesngapps.api.restapi.states.urls.lga', namespace='lga')),
]
