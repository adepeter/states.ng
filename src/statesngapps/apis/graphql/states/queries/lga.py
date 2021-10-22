import graphene

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from ..types.lga import LGAType
from .....states.models import LGA


class LGAQuery:
    lga_by_name = graphene.Field(
        LGAType,
        lga_name=graphene.String(
            description=_('Name of Local Government'),
            required=True,
        ),
        required=True,
        description=_('Local government detail after been queried by LGA name')
    )
    lga_by_short_code = graphene.Field(
        LGAType,
        lga_short_code=graphene.String(
            description=_('Three short characters of Local Government'),
            required=True,
        ),
        required=True,
        description=_('Local government detail after been queried by LGA short code')
    )
    lgas_by_state_name = graphene.List(
        graphene.NonNull(
            LGAType
        ),
        state_name=graphene.String(
            description=_('Name of state name'),
            required=True
        ),
        required=True,
        description=_('All local governments fetched by state name')
    )
    lgas_by_state_short_code = graphene.List(
        graphene.NonNull(
            LGAType
        ),
        state_short_code=graphene.String(
            description=_('State short code'),
            required=True
        ),
        description=_('All local governments fetched by state short code')
    )

    search_lga = graphene.List(
        LGAType,
        lga_name=graphene.String(
            description=_('Keyword of LGA to search for'),
            required=True
        ),
        description=_('Search a LGA'),
    )

    def resolve_lgas_by_state_name(self, info, state_name):
        return LGA.objects.filter(state__name__iexact=state_name)

    def resolve_lga_by_name(self, info, name):
        return get_object_or_404(LGA, name__iexact=name)

    def resolve_lga_by_short_code(self, info, short_code):
        return get_object_or_404(LGA, short_code__iexact=short_code)

    def resolve_lgas_by_state_short_code(self, info, state_short_code):
        return LGA.objects.filter(state__short_code__iexact=state_short_code)

    def resolve_search_lga(self, info, lga_name, **kwargs):
        return LGA.objects.filter(name__icontains=lga_name)
