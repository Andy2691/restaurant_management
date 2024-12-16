from django.db import models
from restaurants.models import Restaurant


class MenuItem(models.Model):
    """
    Modelo para los elementos del menú
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menu_items"
    )

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
