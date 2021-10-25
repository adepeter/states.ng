from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..serializers.auth import AuthenticationSerializer


class LoginAPIView(GenericAPIView):
    serializer_class = AuthenticationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.META.get('HTTP_USER_AGENT'))
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
