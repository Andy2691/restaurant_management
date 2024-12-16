from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer
from .filters import MenuItemFilter  # Importar la clase de filtro


class MenuItemListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear elementos del menú con filtros
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]  # Backend de filtros
    filterset_class = MenuItemFilter  # Clase de filtros personalizada


class MenuItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener detalles, actualizar y eliminar un elemento del menú
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
