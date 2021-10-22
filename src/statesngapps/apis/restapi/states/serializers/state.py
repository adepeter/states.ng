from rest_framework import serializers

from .lga import LGASerializer
from .....states.models import State


class StateSerializer(serializers.ModelSerializer):
    localgovernmentareas = LGASerializer(many=True)

    class Meta:
        model = State
        fields = [
            'name',
            'capital',
            'short_code',
            'localgovernmentareas',
            'website',
            'map',
            'geo_zone'
        ]
