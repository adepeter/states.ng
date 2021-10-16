from django.utils.translation import gettext_lazy as _

from ..behaviours.lga import LocalGovernmentAreaMixin


class LocalGovernmentArea(LocalGovernmentAreaMixin):
    pass


class LGA(LocalGovernmentArea):
    class Meta:
        proxy = True
        verbose_name = _('LGA')
        verbose_name_plural = _('LGAs')
