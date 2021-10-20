from django.conf import settings
from graphene_django.views import GraphQLView

from .schema import schema as root_schema


class GQLPlaygroundView(GraphQLView):
    schema = root_schema
    graphiql = settings.DEBUG
