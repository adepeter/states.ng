from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from .....states.models import LGA, State
from ..serializers.lga import LGASerializer, LGASearchSerializer


class ListLGAsAPIView(ListAPIView):
    serializer_class = LGASerializer
    queryset = LGA.objects.all()


class ListLGAsForStateAPIView(RetrieveModelMixin, ListAPIView):
    serializer_class = LGASerializer

    def get_object(self):
        return get_object_or_404(State, name__icontains=self.kwargs['state'])

    def get_queryset(self):
        state = self.get_object()
        return state.lgas.all()


class SearchLGAAPIView(ListAPIView):
    http_method_names = ['post']
    serializer_class = LGASearchSerializer
    queryset = LGA.objects.all()

    def get_queryset(self):
        qs = super().get_queryset().select_related('state')
        return qs.filter(name__icontains=self.request.data.get('name'))

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            lgas = self.get_queryset()
            serializer = self.get_serializer(lgas, many=True)
            return Response(serializer.data)
        return Response(serializer.errors)
