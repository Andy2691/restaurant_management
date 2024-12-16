from django.urls import path
from .views import RestaurantListCreateView, RestaurantDetailView

app_name = "restaurants"

urlpatterns = [
    path(
        "", RestaurantListCreateView.as_view(), name="restaurant_list_create"
    ),  # Listar y crear restaurantes
    path(
        "<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant_detail_update_delete",
    ),  # Detalle de un restaurante
]
