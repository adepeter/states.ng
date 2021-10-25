from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework import serializers

from django.utils.translation import gettext_lazy as _


class AuthenticationSerializer(serializers.Serializer):
    token = serializers.CharField(
        source='token.key',
        label=_('Token'),
        read_only=True,
        help_text=_('Token for authentication')
    )
    username = serializers.CharField(
        label=_('Username or E-mail address'),
        write_only=True
    )
    password = serializers.CharField(
        label=_('Password'),
        min_length=5,
        max_length=20,
        write_only=True,
        help_text=_(' Password min: 5 , max: 20'),
        trim_whitespace=False
    )

    def validate_username(self, username):
        user_exist = UserWarning.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).exists()
        if not user_exist:
            raise serializers.ValidationError(_('%(username)s does not exist') % {'username': username})
        return username

    def validate(self, attrs):
        request = self.context.get('request')
        username = attrs.pop('username')
        password = attrs.pop('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                _('Supplied credentials are not valid')
            )
        attrs.update({'token': user.auth_token})
        return attrs
