import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):
    """
    Filtro para el modelo User
    """

    typology = django_filters.ChoiceFilter(choices=User.ROLE_CHOICES)  # Filtrar por rol
    active = django_filters.BooleanFilter(
        field_name="active"
    )  # Filtrar por usuarios activos/inactivos
    email = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Buscar usuarios por correo electrónico

    class Meta:
        model = User
        fields = ["typology", "active", "email"]  # Campos filtrables
