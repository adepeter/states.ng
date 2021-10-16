from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from .....states.models import LGA


class LGAType(DjangoObjectType):

    class Meta:
        model = LGA
        exclude = [
            'id'
        ]
        description = _('LGA Object in Nigeria')
