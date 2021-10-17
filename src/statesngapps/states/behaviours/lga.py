from django.db import models
from django.utils.translation import gettext_lazy as _
from tests.hosts import blank

from .name import NameMixin


class LocalGovernmentAreaMixin(NameMixin):
    state = models.ForeignKey(
        'states.State',
        on_delete=models.CASCADE,
        related_name='%(class)ss',
        help_text=_('State LGA belongs to')
    )
    short_code = models.CharField(
        verbose_name=_('Short code'),
        max_length=3,
        db_index=True,
        blank=True,
        help_text=_('Three characters unique identifier of LGA')
    )
    zip_code = models.CharField(
        verbose_name=_('Zip Code'),
        max_length=6,
        db_index=True,
        blank=True,
        help_text=_('Zipcode for LGA')
    )

    def save(self, *args, **kwargs):
        if not self.zip_code:
            self.zip_code = self.state.postal_code
        if not self.short_code:
            if len(self.name) <= 4:
                try:
                    self.short_code = self.name[:3]
                except IndexError:
                    self.short_code = self.name[:-1]
            else:
                self.short_code = self.name[0] + self.name[2] + self.name[-2]
        self.short_code = self.short_code.upper()
        super().save(*args, **kwargs)

    class Meta(NameMixin.Meta):
        abstract = True
        verbose_name = _('Local Government Area')
        verbose_name_plural = _('Local Government Areas')
        constraints = [
            models.UniqueConstraint(fields=['state', 'name'], name='unique_lga_name_and_state'),
            models.UniqueConstraint(fields=['state', 'short_code'], name='unique_lga_shrt_code_and_state')
        ]
        ordering = [
            'name'
        ]
