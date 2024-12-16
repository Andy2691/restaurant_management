from django.db import models
from restaurants.models import Restaurant


class User(models.Model):
    ROLE_CHOICES = [("dealer", "Dealer"), ("customer", "Customer")]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    typology = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")
    phone = models.CharField(max_length=20, blank=True, null=True)
    default_address = models.TextField(blank=True, null=True)
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True,
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
