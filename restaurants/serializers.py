from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Restaurant
    """

    class Meta:
        model = Restaurant
        fields = "__all__"
