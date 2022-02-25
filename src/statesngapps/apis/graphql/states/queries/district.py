import graphene

from django.utils.translation import gettext_lazy as _
from graphql import GraphQLError

from .....states.models import District
from ..types.district import DistrictType


class DistrictQuery:
    all_districts_by_lga_name = graphene.List(
        graphene.NonNull(
            DistrictType
        ),
        lga_name=graphene.String(
            description=_('Local Government Name'),
            required=True
        ),
        description=_('All Districts in a local government when been queried by LGA name'),
        required=True
    )
    all_districts_by_lga_short_code = graphene.List(
        graphene.NonNull(
            DistrictType
        ),
        lga_short_code=graphene.String(
            description=_('Local Government Short Code'),
            required=True
        ),
        description=_('All Districts in a local government when been queried by LGA short code'),
        required=True
    )
    all_districts_in_a_state = graphene.List(
        graphene.NonNull(
            DistrictType
        ),
        state_name=graphene.String(
            description=_('State name'),
        ),
        state_postal_code=graphene.String(
            description=_('State Postal Code'),
        ),
        state_short_code=graphene.String(
            description=_('State short code'),
        ),
        description=_('All Districts in a state when been queried by any state parameter'),
        required=True
    )

    def resolve_all_districts_in_a_state(self, info, **kwargs):
        if not kwargs:
            raise GraphQLError(_('Cannot call query without params'))
        new_fields = {}
        if 'state_name' in kwargs:
            new_fields['lga__state__name__icontains'] = kwargs['state_name']
        if 'short_code' in kwargs:
            new_fields['lga__state___short_code__iexact'] = kwargs['state_short_code']
        if 'state_postal_code' in kwargs:
            new_fields['lga__state__psostal_code__exact'] = kwargs['state_postal_code']
        return District.objects.filter(**new_fields)

    def resolve_all_districts_by_lga_short_code(self, info, lga_short_code):
        return District.objects.filter(lga__short_code__icontains=lga_short_code)

    def resolve_all_districts_by_lga_name(self, info, lga_name):
        return District.objects.filter(lga__name__icontains=lga_name)

    class Meta:
        description = _('District Query')
