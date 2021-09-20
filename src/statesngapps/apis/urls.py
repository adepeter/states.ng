from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('graphql/', include('statesngapps.api.graphql.urls', namespace='graphql')),
    path('restapi/', include('statesngapps.api.restapi.urls', namespace='restapi')),
]
