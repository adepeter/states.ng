from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'restapi'

urlpatterns = [
    path('', include('statesngapps.api.restapi.states.urls', namespace='states')),
]

urlpatterns += [
    path('docs/', include([
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/', SpectacularSwaggerView.as_view(url_name='statesng:restapi:schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='statesng:restapi:schema'), name='redoc'),
    ]))
]
