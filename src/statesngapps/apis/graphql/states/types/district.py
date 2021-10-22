from graphene_django import DjangoObjectType
from django.utils.translation import gettext_lazy as _

from .....states.models import District


class DistrictType(DjangoObjectType):
    class Meta:
        model = District
        exclude = [
            'id'
        ]
        description = _('District object type for STATESNG')
