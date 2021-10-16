from django.urls import path, include

app_name = 'statesng'

urlpatterns = [
    path('', include('statesngapps.admin.urls', namespace='admin')),
    path('', include('statesngapps.states.urls', namespace='states')),
    path('', include('statesngapps.apis.urls', namespace='api')),
]
