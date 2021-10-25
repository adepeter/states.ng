from django.contrib import admin

# Register your models here.
from ..models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'user_agent',
        'token',
        'date_logged'
    ]
    list_filter = [
        'user'
    ]
    readonly_fields = [
        'token'
    ]
    date_hierarchy = 'date_logged'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user', 'user_agent', 'token', 'date_logged']
        else:
            return []


__all__ = [
    'DeviceAdmin'
]
