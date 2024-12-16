from django.urls import path
from .views import RestaurantListCreateView, RestaurantDetailView

urlpatterns = [
    path(
        "", RestaurantListCreateView.as_view(), name="restaurant_list_create"
    ),  # GET y POST
    path(
        "<int:pk>/", RestaurantDetailView.as_view(), name="restaurant_detail"
    ),  # GET, PUT, PATCH y DELETE
]
