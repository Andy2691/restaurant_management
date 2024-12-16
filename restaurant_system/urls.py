from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger para la documentación de la API
schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant Management API",
        default_version="v1",
        description="Documentación de la API para la gestión de pedidos de restaurantes",
    ),
    public=True,
)

urlpatterns = [
    # Rutas del administrador de Django
    path("admin/", admin.site.urls),
    # Rutas de autenticación con JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Rutas de aplicaciones principales
    path("api/menu-items/", include("menu_items.urls", namespace="menu_items")),
    path("api/users/", include("users.urls", namespace="users")),
    path("api/restaurants/", include("restaurants.urls", namespace="restaurants")),
    path("api/orders/", include("orders.urls", namespace="orders")),
    # Documentación de la API
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
