from graphene_django import DjangoObjectType

from django.utils.translation import gettext_lazy as _

from ....states.models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City
        fields = '__all__'
        description = _('City object in Nigeria')
