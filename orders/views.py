from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter


class OrderListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear pedidos
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter  # Clase de filtros personalizada


class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener detalles, actualizar y eliminar un pedido
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
