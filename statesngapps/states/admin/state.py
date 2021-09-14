from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from .lga import LGAInline
from ..models import State, Governor


class GovernorInline(admin.StackedInline):
    model = Governor


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'short_code',
        'capital',
        'slogan',
        'get_current_governor',
        'website',
        'get_lgas_count',
        'get_governors_count',
        'get_cities_count',
    ]
    # inlines = [
    #     # GovernorInline,
    #     # LGAInline
    # ]

    @admin.display(description=_('Current governor'))
    def get_current_governor(self, state):
        return Governor.objects. \
            select_related('state'). \
            filter(state=state). \
            get(is_current=True)

    @admin.display(description=_('Total LGAs'))
    def get_lgas_count(self, state):
        return state.total_lgas

    @admin.display(description=_('Total Cities'))
    def get_cities_count(self, state):
        return state.total_cities

    @admin.display(description=_('Total governors'))
    def get_governors_count(self, state):
        return state.total_governors

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            total_cities=Count('cities'),
            total_governors=Count('governors'),
            total_lgas=Count('lgas')
        )


__all__ = [
    'StateAdmin'
]
