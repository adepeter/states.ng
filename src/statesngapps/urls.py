from django.urls import path, include

app_name = 'statesng'

urlpatterns = [
    path('', include('statesngapps.admin.urls', namespace='admin')),
    path('home/', include('statesngapps.home.urls', namespace='home')),
    path('pages/', include('statesngapps.pages.urls', namespace='pages')),
    path('search/', include('statesngapps.search.urls', namespace='search')),
    path('', include('statesngapps.states.urls', namespace='states')),
    path('', include('statesngapps.apis.urls', namespace='api')),
]
