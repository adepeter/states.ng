from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from .....states.models import LGA


class LGAType(DjangoObjectType):

    class Meta:
        model = LGA
        fields = '__all__'
        description = _('LGA Object in Nigeria')
