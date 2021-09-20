from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('graphql/', include('statesngapps.apis.graphql.urls', namespace='graphql')),
    path('restapi/', include('statesngapps.apis.restapi.urls', namespace='restapi')),
]
