from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.flatpages.models import FlatPage as BaseFlatPageModel
from django.utils.translation import gettext_lazy as _

from ..models import FlatPage


@admin.register(FlatPage)
class FlatPageAdmin(BaseFlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


admin.site.unregister(BaseFlatPageModel)

__all__ = [
    'FlatPageAdmin'
]
