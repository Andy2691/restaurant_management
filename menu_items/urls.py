from django.urls import path
from .views import MenuItemListCreateView, MenuItemRetrieveUpdateDestroyView

app_name = "menu_items"

urlpatterns = [
    path(
        "", MenuItemListCreateView.as_view(), name="menu_item_list_create"
    ),  # Listar y crear elementos del menú
    path(
        "<int:pk>/",
        MenuItemRetrieveUpdateDestroyView.as_view(),
        name="menu_item_detail_update_delete",
    ),  # Detalle de un elemento del menú
]
