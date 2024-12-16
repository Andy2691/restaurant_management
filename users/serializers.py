from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User con validaciones adicionales
    """

    class Meta:
        model = User
        fields = "__all__"

    def validate_email(self, value):
        """
        Validar que el correo sea único
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está registrado.")
        return value

    def validate_password(self, value):
        """
        Validar y encriptar contraseñas
        """
        if len(value) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres."
            )
        return make_password(value)
