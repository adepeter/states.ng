from django.urls import path, include

app_name = 'statesng'

urlpatterns = [
    path('', include('statesngapps.states.urls', namespace='states')),
]
