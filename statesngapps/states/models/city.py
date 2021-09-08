from django.db import models
from django.utils.translation import gettext_lazy as _

from ..behaviours.name import NameMixin


class City(NameMixin):
    state = models.ForeignKey(
        'states.State',
        on_delete=models.CASCADE,
        related_name='cities'
    )

    class Meta:
        verbose_name_plural = _('Cities')
