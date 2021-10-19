from django.views.generic import TemplateView

TEMPLATE_URL = 'home'


class HomeView(TemplateView):
    template_name = f'{TEMPLATE_URL}/index.html'
