import django_filters
from .models import Order


class OrderFilter(django_filters.FilterSet):
    """
    Filtro para el modelo Order
    """

    status = django_filters.ChoiceFilter(
        choices=Order.STATUS_CHOICES
    )  # Filtrar por estado
    restaurant = django_filters.NumberFilter(
        field_name="restaurant__id", lookup_expr="exact"
    )  # Restaurante exacto
    customer = django_filters.NumberFilter(
        field_name="customer__id", lookup_expr="exact"
    )  # Cliente exacto
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at"
    )  # Rango de fechas

    class Meta:
        model = Order
        fields = ["status", "restaurant", "customer", "created_at"]
