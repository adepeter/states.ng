import graphene
from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from .lga import LGAType
from .....states.models import State, LGA, Governor


class StateGeoZoneEnum(graphene.Enum):
    ZONE_NORTH_CENTRAL = State.ZONE_NORTH_CENTRAL
    NORTH_EAST = State.ZONE_NORTH_EAST
    NORTH_WEST = State.ZONE_NORTH_WEST
    SOUTH_EAST = State.ZONE_SOUTH_EAST
    SOUTH_SOUTH = State.ZONE_SOUTH_SOUTH
    SOUTH_WEST = State.ZONE_SOUTH_WEST


class StateType(DjangoObjectType):
    lgas = graphene.List(
        LGAType,
        description=_('LGAs in the state')
    )

    def resolve_lgas(self, info):
        return LGA.objects.filter(state=self)

    class Meta:
        model = State
        exclude = [
            'id'
        ]
        description = _('State Object in Nigeria')


class StateCountType(graphene.ObjectType):
    total = graphene.Int(
        description=_('Total number of states')
    )


class GovernorType(DjangoObjectType):
    class Meta:
        model = Governor
        fields = '__all__'
        description = _('Governor Object in Nigeria')
