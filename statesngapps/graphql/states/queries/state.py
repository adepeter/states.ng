import graphene
from django.shortcuts import get_object_or_404

from django.utils.translation import gettext_lazy as _

from ....states.models import State
from ..types.state import StateType, StateCountType


class StateQuery:
    count_states = graphene.Field(
        StateCountType,
        description=_('Total number of states')
    )
    all_states = graphene.List(
        StateType,
        description=_('List of all states in Nigeria'),
        required=True,
    )
    search_state = graphene.Field(
        StateType,
        description=_('Get a specific state info'),
        state_name=graphene.String(),
        short_code=graphene.String(),
        required=True
    )

    def resolve_search_state(self, info, **kwargs):
        fields = {}
        for kwarg in kwargs:
            fields.update({kwarg + '__iexact': kwargs[kwarg]})
        return get_object_or_404(State, **fields)

    def resolve_count_states(self, info):
        return {'total': State.objects.count()}

    def resolve_all_states(self, info):
        return State.objects.all()
