from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "", UserListCreateView.as_view(), name="user_list_create"
    ),  # Listar y crear usuarios
    path(
        "<int:pk>/",
        UserRetrieveUpdateDestroyView.as_view(),
        name="user_detail_update_delete",
    ),  # Detalle, actualizar y eliminar usuarios
]
