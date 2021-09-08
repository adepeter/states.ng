import graphene

from django.utils.translation import gettext_lazy as _

from .states.schema import StatesRootQueries


class Query(StatesRootQueries, graphene.ObjectType):
    class Meta:
        description = _('Entry Point to get State Data in Nigeria')


schema = graphene.Schema(query=Query)
