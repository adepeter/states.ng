from django.urls import path, include
from django.views.generic import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'restapi'

urlpatterns = [
    path('', include('statesngapps.apis.restapi.states.urls', namespace='states')),
    path('', TemplateView.as_view(template_name='apis/restapi/index.html'), name='index'),
]

urlpatterns += [
    path('docs/', include([
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/', SpectacularSwaggerView.as_view(url_name='statesng:api:restapi:schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='statesng:api:restapi:schema'), name='redoc'),
    ]))
]
