from django.contrib import admin

from ..models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'state',
        'name',
    ]


__all__ = [
    'CityAdmin'
]
