import graphene
from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from .lga import LGAType
from ....states.models import State, LGA


class StateType(DjangoObjectType):
    lgas = graphene.List(
        LGAType,
        description=_('LGAs in the state')
    )

    def resolve_lgas(self, info):
        return LGA.objects.filter(state=self)

    class Meta:
        model = State
        fields = '__all__'
        description = _('State Object in Nigeria')


class StateCountType(graphene.ObjectType):
    total = graphene.Int(
        description=_('Total number of states')
    )
