from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear elementos del menú
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener detalles, actualizar y eliminar un elemento del menú
    """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
