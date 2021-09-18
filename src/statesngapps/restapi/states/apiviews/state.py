from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.mixins import RetrieveModelMixin

from ..serializers.lga import LGASerializer
from ..serializers.state import StateSerializer
from ....states.models import State


class ListStatesAPIView(ListAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class RetrieveStateAPIView(RetrieveAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    lookup_url_kwarg = 'state'
    lookup_field = 'name__icontains'


class ListLGAsForStateAPIView(RetrieveModelMixin, ListAPIView):
    serializer_class = LGASerializer

    def get_object(self):
        return get_object_or_404(State, name__icontains=self.kwargs['state'])

    def get_queryset(self):
        state = self.get_object()
        return state.lgas.all()


class ListCitiesInStateAPIView(RetrieveModelMixin, ListAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()
