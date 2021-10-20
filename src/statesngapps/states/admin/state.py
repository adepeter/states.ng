from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe
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
        'creation_date',
        'postal_code',
        'get_current_governor',
        'website',
        'get_lgas_count',
        'get_military_government_count',
        'get_governors_count',
        'get_cities_count',
    ]
    list_filter = [
        'geo_zone'
    ]

    fieldsets = [
        (_('Basic'), {
            'description': _('Basic info of state'),
            'fields': ['name', 'short_code', 'capital', 'slogan', 'postal_code', 'website']
        }),
        (_('Map'), {
            'fields': ['map_preview', 'map', 'geo_zone']
        }),
        (_('Important dates'), {
            'fields': ['creation_date']
        })
    ]

    readonly_fields = [
        'map_preview'
    ]
    date_hierarchy = 'creation_date'
    save_on_top = True

    @admin.display(description=_('Preview of state map'), empty_value=_('No map yet'))
    def map_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" alt="{alt}" />'.format(
            url=obj.map.url,
            width=128,
            height=128,
            alt=obj.name
        )
        )

    # inlines = [
    #     # GovernorInline,
    #     LGAInline
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

    @admin.display(description=_('Total Military Governors'))
    def get_military_government_count(self, state):
        return state.total_governors

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            total_cities=Count('cities'),
            total_governors=Count('governors'),
            total_lgas=Count('localgovernmentareas')
        )


@admin.register(Governor)
class GovernorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'state',
        'government',
        'date_started',
        'date_ended',
        'is_current'
    ]
    list_filter = [
        'government',
        'is_current',
        'state'
    ]
    ordering = [
        'date_started',
        '-date_ended'
    ]


__all__ = [
    'StateAdmin',
    'GovernorAdmin'
]
