from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ....states.models import LGA
from ..serializers.lga import LGASerializer, LGASearchSerializer


class ListLGAsAPIView(ListAPIView):
    serializer_class = LGASerializer
    queryset = LGA.objects.all()


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
