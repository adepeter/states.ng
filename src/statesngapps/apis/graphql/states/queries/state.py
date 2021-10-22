import graphene
from IPython.core.release import description
from django.shortcuts import get_object_or_404

from django.utils.translation import gettext_lazy as _

from ..types.inputs.state import StateInputType
from .....states.models import State, Governor
from ..types.state import StateType, StateCountType, GovernorType, StateGeoZoneEnum


class StateQuery:
    all_states = graphene.List(
        StateType,
        description=_('List of all states in Nigeria'),
        required=True,
    )
    all_states_by_geo_political_zone = graphene.List(
        graphene.NonNull(StateType, description=_('State')),
        geo_political_zone=graphene.String(required=True, description=_('Geopolitical Zone')),
        description=_('Lists of all States based on their geo political zones'),
    )
    search_state = graphene.Field(
        StateType,
        description=_('Get a specific state info'),
        state_name=graphene.String(required=True),
        short_code=graphene.String(),
        required=True
    )

    def resolve_all_states_by_geo_political_zone(self, info, geo_political_zone):
        return State.objects.filter(geo_zone__iexact=geo_political_zone)

    def resolve_search_state(self, info, **kwargs):
        fields = {}
        for kwarg in kwargs:
            fields.update({kwarg + '__iexact': kwargs[kwarg]})
        return get_object_or_404(State, **fields)

    def resolve_all_states(self, info):
        return State.objects.all()


class GovernorQuery:
    all_governors = graphene.List(
        graphene.NonNull(
            GovernorType
        ),
        description=_('List of all governors in Nigeria')
    )
    all_governors_by_state = graphene.List(
        graphene.NonNull(
            GovernorType
        ),
        state=graphene.Argument(StateInputType),
        description=_('List of all governors by state name or state short code')
    )

    def resolve_all_governors(self, info):
        return Governor.objects.select_related('state').all()

    def resolve_all_governors_by_state(self, info, state, **kwargs):
        return Governor.objects.select_related('state').filter(state__name__iexact=state)
