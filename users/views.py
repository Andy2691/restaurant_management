from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from .filters import UserFilter


class UserListView(ListAPIView):
    """
    Vista para listar usuarios con filtros
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter  # Clase de filtros personalizada


class RegisterUserView(APIView):
    """
    Vista para registrar nuevos usuarios
    """

    permission_classes = [AllowAny]  # Permitir acceso público

    def post(self, request):
        # Usar el serializador para validar y crear un usuario
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
