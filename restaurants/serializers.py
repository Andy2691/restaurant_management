from rest_framework import serializers
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
        extra_kwargs = {
            "rating": {"required": False},
            "status": {"required": False},
            "category": {"required": False},
            "latitude": {"required": False},
            "longitude": {"required": False},
        }
