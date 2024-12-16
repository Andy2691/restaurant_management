from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear usuarios
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener detalles, actualizar y eliminar un usuario
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
