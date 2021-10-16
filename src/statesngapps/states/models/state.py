from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from tests.hosts import blank

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
    map = models.ImageField(
        verbose_name=_('State map'),
        upload_to='states',
        blank=True,
        help_text=_('Map of the state')
    )
    postal_code = models.CharField(
        verbose_name=_('Postal code'),
        max_length=6,
        default='000001',
        blank=True,
        help_text=_('Postal Code to find state')
    )
    creation_date = models.DateField(
        verbose_name=_('Creation date'),
        default=timezone.now,
        help_text=_('Date state was created'),
    )

    class Meta(NameMixin.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'postal_code'],
                name='unique_name_on_postal_code'
            )
        ]

    def save(self, *args, **kwargs):
        if not self.website:
            self.website = slugify(self.name).replace('-', '')
            self.website = 'https://' + self.website + 'state.gov.ng'
        super().save(*args, **kwargs)


class Governor(NameMixin):
    GOVERNMENT_MILITARY = 'military'
    GOVERNMENT_DEMOCRACY = 'democracy'

    __GOVERNMENT_CHOICES = (
        (GOVERNMENT_MILITARY, _('Military')),
        (GOVERNMENT_DEMOCRACY, _('Democracy')),
    )
    government = models.CharField(
        verbose_name=_('government type'),
        max_length=10,
        choices=__GOVERNMENT_CHOICES,
        null=True,
        help_text=_('System of government')
    )
    state = models.ForeignKey(
        verbose_name=_('State'),
        to=State,
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
