from django.db import models
from django.utils.translation import gettext_lazy as _


class NameMixin(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']
