from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from ..models import State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_code',
        'capital',
        'slogan',
        'get_lgas_count',
        'get_cities_count',
    ]
    # ordering = [
    #     'get_cities_count',
    #     'get_lgas_count'
    # ]

    @admin.display(description=_('Total LGAs'))
    def get_lgas_count(self, state):
        return state.total_lgas

    @admin.display(description=_('Total Cities'))
    def get_cities_count(self, state):
        return state.total_cities

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            total_cities=Count('cities'),
            total_lgas=Count('lgas')
        )


__all__ = [
    'StateAdmin'
]
