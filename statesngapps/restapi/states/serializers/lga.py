from rest_framework import serializers

from ....states.models import LGA


class LGASerializer(serializers.ModelSerializer):
    class Meta:
        model = LGA
        exclude = [
            'id',
            'state'
        ]
