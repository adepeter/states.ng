from django.contrib import admin

from ..models import LGA


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = [
        'state',
        'name',
        'short_code',
        'zip_code'
    ]


__all__ = [
    'LGAAdmin'
]
