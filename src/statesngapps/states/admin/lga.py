from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.translation import gettext_lazy as _

from .district import DistrictInline
from ..models import LGA


class LGAInline(admin.StackedInline):
    model = LGA
    extra = 10


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display_links = [
        'name'
    ]
    list_display = [
        'name',
        'state',
        'short_code',
        'zip_code'
    ]
    list_filter = [
        'state'
    ]
    list_editable = [
        'short_code',
        'zip_code'
    ]
    inlines = [
        DistrictInline
    ]
    readonly_fields = [
        'get_districts'
    ]

    @admin.display(description=_('List of districts'), empty_value=_('No districts yet'))
    def get_districts(self, obj):
        districts_qs = obj.districts.all()
        districts = ''
        for index in range(districts_qs.count()):
            districts += districts_qs[index].name
            if districts_qs.count() - 2 == index:
                districts += ' and '
            elif districts_qs.count() - 1 == index:
                continue
            else:
                districts += ', '
        return districts


__all__ = [
    'LGAAdmin',
    'LGAInline'
]
