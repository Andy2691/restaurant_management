from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo MenuItem con validaciones adicionales
    """

    class Meta:
        model = MenuItem
        fields = "__all__"

    def validate_price(self, value):
        """
        Validar que el precio sea mayor que 0
        """
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que 0.")
        return value
