from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import GQLPlaygroundView as GraphQLPlaygroundView

app_name = 'graphql'

urlpatterns = [
    path('', csrf_exempt(GraphQLPlaygroundView.as_view()), name='playground'),
]
