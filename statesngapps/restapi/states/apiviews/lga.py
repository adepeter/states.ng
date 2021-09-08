from rest_framework.generics import ListAPIView

from ....states.models import LGA
from ..serializers.lga import LGASerializer


class ListLGAsAPIView(ListAPIView):
    serializer_class = LGASerializer
    queryset = LGA.objects.all()
