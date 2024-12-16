from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear restaurantes
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetailView(RetrieveUpdateDestroyAPIView):
    """
    Vista para detalles, actualización y eliminación de un restaurante
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
