from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Order con validaciones adicionales
    """

    class Meta:
        model = Order
        fields = "__all__"

    def validate_status(self, value):
        """
        Validar que el estado sea válido
        """
        valid_statuses = ["PENDING", "PREPARING", "DELIVERED", "CANCELLED"]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Estado no válido: {value}")
        return value

    def validate(self, data):
        """
        Validación global: total_amount debe coincidir con la suma de subtotales
        """
        order_items = self.instance.order_items.all() if self.instance else []
        calculated_total = sum(item.subtotal for item in order_items)
        if data["total_amount"] != calculated_total:
            raise serializers.ValidationError(
                "El total del pedido no coincide con la suma de los subtotales."
            )
        return data


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo OrderItem con validaciones adicionales
    """

    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate_quantity(self, value):
        """
        Validar que la cantidad sea mayor que 0
        """
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que 0.")
        return value

    def validate(self, data):
        """
        Validar que el menú pertenezca al restaurante del pedido
        """
        order = data.get("order")
        menu_item = data.get("menu_item")

        if menu_item and order and menu_item.restaurant != order.restaurant:
            raise serializers.ValidationError(
                "El elemento del menú no pertenece al restaurante del pedido."
            )
        return data
