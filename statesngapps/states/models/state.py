from django.db import models
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

    def __str__(self):
        return self.name
