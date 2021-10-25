from django.urls import include, path

app_name = 'users'

urlpatterns = [
    path('auth/', include('statesngapps.apis.restapi.users.urls.auth', namespace='auth')),
]
