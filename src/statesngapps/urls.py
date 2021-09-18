from django.urls import path, include

app_name = 'statesng'

urlpatterns = [
    path('graphql/', include('statesngapps.graphql.urls', namespace='graphql')),
    path('restapi/', include('statesngapps.restapi.urls', namespace='restapi')),
    path('', include('statesngapps.states.urls', namespace='states')),
]
