from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        related_name="booking_user",
        on_delete=models.CASCADE,
    )
    number_of_passengers = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    bus_route = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    destination = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    amount_paid = models.CharField(
        max_length=100,
    	null=True,
        blank=True
    )

class Destinations(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )