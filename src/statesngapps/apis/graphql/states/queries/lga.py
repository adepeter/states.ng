import graphene

from django.utils.translation import gettext_lazy as _

from ..types.lga import LGAType
from src.statesngapps.states.models import LGA


class LGAQuery:
    all_lgas = graphene.List(
        LGAType,
        description=_('List of all LGAs in Nigeria'),
        state_name=graphene.String(
            description=_('State name to use get LGAs'),
        ),
        state_short_code=graphene.String(
            description=_('State Short code to use get LGAs'),
        ),
        state_capital_name=graphene.String(
            description=_('State capital name to use get LGAs'),
        ),
        required=True,
    )
    search_lga = graphene.List(
        LGAType,
        lga_name=graphene.String(
            description=_('Keyword of LGA to search for'),
            required=True
        ),
        description=_('Search a LGA'),
    )

    def resolve_search_lga(self, info, lga_name, **kwargs):
        return LGA.objects.filter(name__icontains=lga_name)

    def resolve_all_lgas(self, info, **kwargs):
        state_name = kwargs['state_name']
        if state_name:
            return LGA.objects.filter(state__name__iexact=state_name)
        elif kwargs['state_capital_name']:
            return LGA.objects.filter(state__capital__iexact=kwargs['state_capital_name'])
        elif kwargs['state_short_code']:
            return LGA.objects.filter(state__short_code__iexact=kwargs['state_short_code'])
        else:
            return LGA.objects.all()
