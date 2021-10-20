from django.urls import include, path

app_name = 'pages'

urlpatterns = [
    path('contact/', include('statesngapps.pages.urls.contact', namespace='contact')),
    path('api/', include('statesngapps.pages.urls.api', namespace='api')),
]
