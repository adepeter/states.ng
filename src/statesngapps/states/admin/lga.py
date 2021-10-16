from django.contrib import admin

from ..models import LGA


class LGAInline(admin.StackedInline):
    model = LGA
    extra = 10


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = [
        'state',
        'name',
        'short_code',
        'zip_code'
    ]
    list_filter = [
        'state'
    ]

__all__ = [
    'LGAAdmin',
    'LGAInline'
]
