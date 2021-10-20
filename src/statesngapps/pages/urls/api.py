from django.urls import path

from ..views.api import RestAPILandingView, GraphQLLandingView

app_name = 'api'

urlpatterns = [
    path('graphql/', GraphQLLandingView.as_view(), name='graphql'),
    path('restapi/', RestAPILandingView.as_view(), name='restapi'),
]
