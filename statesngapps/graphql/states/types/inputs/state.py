import graphene


class StateInputType(graphene.InputObjectType):
    state_name = graphene.String()
    state_short_code = graphene.String()
