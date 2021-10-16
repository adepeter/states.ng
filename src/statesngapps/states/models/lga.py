from django.db import models
from django.utils.translation import gettext_lazy as _

from ..behaviours.name import NameMixin


class LocalGovernmentArea(NameMixin):
    state = models.ForeignKey(
        'states.State',
        on_delete=models.CASCADE,
        related_name='lgas',
        help_text=_('State LGA belongs to')
    )
    short_code = models.CharField(
        verbose_name=_('Short code'),
        max_length=3,
        db_index=True,
        help_text=_('Three characters unique identifier of lga')
    )
    zip_code = models.CharField(
        verbose_name=_('Zip Code'),
        max_length=6,
        db_index=True,
        blank=True,
        help_text=_('Zipcode for LGA')
    )

    class Meta:
        verbose_name = _('Local Government Area')
        verbose_name_plural = _('Local Government Areas')
        constraints = [
            models.UniqueConstraint(fields=['state', 'name'], name='unique_lga_name_and_state'),
            models.UniqueConstraint(fields=['state', 'short_code'], name='unique_lga_shrt_code_and_state')
        ]
        ordering = [
            'name'
        ]


class LGA(LocalGovernmentArea):
    class Meta:
        proxy = True
        verbose_name = _('LGA')
        verbose_name_plural = _('LGAs')
