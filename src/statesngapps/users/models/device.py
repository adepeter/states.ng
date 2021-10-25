from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token


class Device(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='devices'
    )
    token = models.CharField(max_length=255, editable=False, blank=True)
    user_agent = models.CharField(max_length=255)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.user_agent} - {self.token}'

    def save(self, *args, **kwargs):
        get_token, created_token = Token.objects.get_or_create(user=self.user)
        if not self.token:
            self.token = get_token.key
        super().save(*args, **kwargs)

    class Meta:
        get_latest_by = 'date_logged'
        ordering = [
            '-date_logged'
        ]
