from django.contrib import admin

from ..models import District


class DistrictInline(admin.StackedInline):
    model = District
    extra = 4


__all__ = [
    'DistrictInline'
]
