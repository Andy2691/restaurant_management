import django_filters
from .models import MenuItem


class MenuItemFilter(django_filters.FilterSet):
    """
    Filtro para el modelo MenuItem
    """

    name = django_filters.CharFilter(lookup_expr="icontains")  # Buscar por nombre
    price = django_filters.RangeFilter()  # Filtrar por rango de precios
    category = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Buscar por categoría
    restaurant = django_filters.NumberFilter(
        field_name="restaurant__id", lookup_expr="exact"
    )  # Filtrar por restaurante

    class Meta:
        model = MenuItem
        fields = ["name", "price", "category", "restaurant"]
