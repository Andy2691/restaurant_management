from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User
    """

    class Meta:
        model = User
        fields = "__all__"
