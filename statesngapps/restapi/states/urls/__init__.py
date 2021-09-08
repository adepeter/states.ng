from django.urls import path, re_path, include

app_name = 'states'

urlpatterns = [
    path('states/', include('statesngapps.restapi.states.urls.state', namespace='state')),
    path('lgas/', include('statesngapps.restapi.states.urls.lga', namespace='lga')),
]
