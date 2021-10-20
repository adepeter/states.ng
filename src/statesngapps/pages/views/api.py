from django.views.generic import TemplateView

TEMPLATE_URL = 'pages/api'


class RestAPILandingView(TemplateView):
    template_name = f'{TEMPLATE_URL}/restapi.html'
    

class GraphQLLandingView(TemplateView):
    template_name = f'{TEMPLATE_URL}/graphql.html'
