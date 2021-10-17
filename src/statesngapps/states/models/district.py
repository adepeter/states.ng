from django.db import models
from django.utils.translation import gettext_lazy as _

from ..behaviours.name import NameMixin


class District(NameMixin):
    lga = models.ForeignKey(
        'states.LocalGovernmentArea',
        on_delete=models.CASCADE,
        related_name='districts',
        help_text=_('LGA district falls under')
    )
