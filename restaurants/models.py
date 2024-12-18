from django.db import models


class Restaurant(models.Model):
    """
    Modelo para Restaurantes
    """

    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=21, decimal_places=11)
    longitude = models.DecimalField(max_digits=21, decimal_places=11)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
