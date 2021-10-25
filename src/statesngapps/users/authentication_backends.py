from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token

from .models import Device

User = get_user_model()


class AuthenticationBackend:
    def authenticate(self, request, username, password, *args, **kwargs):
        user_agent = request.META['HTTP_USER_AGENT']
        email = kwargs.pop('email', None)
        if email is not None:
            username = kwargs['email'].lower()
        if not username and password:
            return None
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                get_token, created_token = Token.objects.get_or_create(user=user)
                try:
                    device = Device.objects.filter(user=user).first()
                    if device.user_agent != user_agent and not created_token:
                        user.auth_token.delete()
                        Token.objects.create(user=user)
                except (Device.DoesNotExist, AttributeError):
                    user.devices.create(user_agent=user_agent, token=get_token.key)
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
