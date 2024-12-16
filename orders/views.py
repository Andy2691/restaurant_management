from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear pedidos
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener detalles, actualizar y eliminar un pedido
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
