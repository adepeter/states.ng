import graphene
from django.shortcuts import get_object_or_404

from django.utils.translation import gettext_lazy as _

from src.statesngapps.states.models import City
from ..types.city import CityType


class CityQuery:
    all_cities = graphene.List(
        CityType,
        state_name=graphene.String(
            description=_('State name filter cities')
        ),
        description=_('Get list of all cities in Nigeria')
    )
    search_city = graphene.Field(
        CityType,
        city_name=graphene.String(
            description=_('City name to search for'),
            required=True
        ),
        description=_('Keyword search for city'),
        required=True
    )

    def resolve_all_cities(self, info, state_name=None):
        if state_name is not None:
            return City.objects.filter(state__name__iexact=state_name)
        return City.objects.all()

    def resolve_search_city(self, info, city_name):
        return get_object_or_404(City, name__iexact=city_name)
