import django_filters
from .models import Restaurant


class RestaurantFilter(django_filters.FilterSet):
    """
    Filtro para el modelo Restaurant
    """

    name = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Buscar por nombre (case-insensitive)
    address = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Buscar por dirección (case-insensitive)

    class Meta:
        model = Restaurant
        fields = ["name", "address"]  # Campos disponibles para filtrar
