from django.contrib.flatpages import views as flatpage_views
from django.urls import include, path

app_name = 'pages'

urlpatterns = [
    path('contact/', include('statesngapps.pages.urls.contact', namespace='contact')),
    path('api/', include('statesngapps.pages.urls.api', namespace='api')),
    path('', include('django.contrib.flatpages.urls')),
]

urlpatterns += [
    path('about-nigeria/', flatpage_views.flatpage, {'url': '/about-nigeria/'}, name='about_nigeria'),
]
