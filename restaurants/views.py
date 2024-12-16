from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Restaurant
from .serializers import RestaurantSerializer
from .filters import RestaurantFilter  # Importar la clase de filtro


class RestaurantListCreateView(ListCreateAPIView):
    """
    Vista para listar y crear restaurantes con filtros
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]  # Backend de filtros
    filterset_class = RestaurantFilter  # Clase de filtros personalizada


class RestaurantDetailView(RetrieveUpdateDestroyAPIView):
    """
    Vista para detalles, actualización y eliminación de un restaurante
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
