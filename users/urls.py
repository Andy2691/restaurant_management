from django.urls import path
from .views import RegisterUserView, UserListView

app_name = "users"

urlpatterns = [
    path(
        "register/", RegisterUserView.as_view(), name="register"
    ),  # Registro de usuarios
    path(
        "", UserListView.as_view(), name="user_list"
    ),  # Listado de usuarios con filtros
]
