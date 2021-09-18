from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from ....states.models import LGA


class LGASerializer(serializers.ModelSerializer):
    class Meta:
        model = LGA
        exclude = [
            'id',
            'state'
        ]


class LGASearchSerializer(LGASerializer):

    name = serializers.CharField(
        label=_('Search keyword'),
        help_text=_('Enter parts of the local government name or short code and options will be returned'),
        write_only=False
    )
    state = serializers.StringRelatedField()

    class Meta:
        model = LGA
        fields = [
            'name',
            'state',
            'zip_code',
        ]
        read_only_fields = [
            'state',
            'zip_code',
        ]
