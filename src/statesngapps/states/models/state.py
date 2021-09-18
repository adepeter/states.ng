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
        db_index=True,
        help_text=_('Capital of state')
    )
    slogan = models.CharField(
        verbose_name=_('slogan'),
        max_length=255,
        help_text=_('Slogan for state')
    )
    short_code = models.CharField(
        verbose_name=_('Short Code'),
        max_length=3,
        unique=True,
        db_index=True,
        help_text=_('Two SHORT CODE to identify a state')
    )
    website = models.URLField(
        verbose_name=_('Website'),
        blank=True,
        null=True,
        help_text=_('Official website of state')
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
        related_name='governors',
        help_text=_('State governing')
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
