from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from ..states.models import State, LocalGovernmentArea

TEMPLATE_URL = 'search'


@method_decorator(cache_page(60 * 5), name='dispatch')
@method_decorator(require_GET, name='dispatch')
class SearchView(ListView):
    model = State
    paginate_by = 10
    template_name = f'{TEMPLATE_URL}/search_result.html'

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        if settings.USING_POSTGRES:
            from django.contrib.postgres.search import SearchVector
            return qs
        return qs.filter(
            Q(name__icontains=search_query) |\
            Q(postal_code__icontains=search_query) |\
            Q(capital__icontains=search_query) |\
            Q(localgovernmentareas__in=[lga for lga in LocalGovernmentArea.objects.filter(
                Q(name__icontains=search_query) |\
                Q(secretariat__icontains=search_query) |\
                Q(zip_code__contains=search_query) |\
                Q(name__icontains=search_query) |\
                Q(districts__name__in=search_query)
            )])
        ).distinct()

    def dispatch(self, request, *args, **kwargs):
        if 'search' not in request.GET:
            return HttpResponseRedirect(reverse('statesng:home:index'))
        return super(SearchView, self).dispatch(request, *args, **kwargs)
