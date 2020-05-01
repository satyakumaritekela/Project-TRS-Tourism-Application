from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# Create your models here.
class AuthToken(models.Model):
    user = models.OneToOneField(
        User,
        related_name="user_token",
        on_delete=models.CASCADE,
    )
    token = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    otp = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )