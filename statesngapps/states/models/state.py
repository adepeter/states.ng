from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..behaviours.name import NameMixin


class State(NameMixin):
    capital = models.CharField(
        verbose_name=_('capital'),
        max_length=255,
        unique=True,
        db_index=True
    )
    slogan = models.CharField(
        verbose_name=_('slogan'),
        max_length=255,
    )
    short_code = models.CharField(
        verbose_name=_('Short Code'),
        max_length=3,
        unique=True,
        db_index=True
    )
    website = models.URLField(
        verbose_name=_('Website'),
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.website:
            self.website = slugify(self.name).replace('-', '')
            self.website = 'https://' + self.website + 'state.gov.ng'
        super().save(*args, **kwargs)


class Governor(NameMixin):
    state = models.ForeignKey(
        verbose_name=_('State'),
        to='states.State',
        on_delete=models.PROTECT,
        related_name='governors'
    )
    date_started = models.DateField(
        verbose_name=_('Start year'),
        default=timezone.now,
        help_text=_('Tenure start date')
    )
    date_ended = models.DateField(
        verbose_name=_('End year'),
        default=timezone.now,
        help_text=_('Tenure end date')
    )
    is_current = models.BooleanField(
        verbose_name=_('Current governor'),
        default=False,
        help_text=_('Currently active as Governor?')
    )
