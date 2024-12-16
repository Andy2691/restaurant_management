import csv
from datetime import datetime
from django.db.models import Count, Sum
from orders.models import Order
from restaurants.models import Restaurant


def generate_sales_report(start_date, end_date, file_path):
    """
    Generar reporte de ventas por restaurante en formato CSV
    """
    # Consulta agregada para calcular ventas y montos totales
    sales_data = Restaurant.objects.annotate(
        total_sales=Count(
            "orders",
            filter=Order.objects.filter(created_at__range=[start_date, end_date]),
        ),
        total_revenue=Sum(
            "orders__total_amount",
            filter=Order.objects.filter(created_at__range=[start_date, end_date]),
        ),
    )

    # Crear el archivo CSV
    with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(
            ["ID Restaurante", "Nombre Restaurante", "Total Ventas", "Total Ingresos"]
        )

        for restaurant in sales_data:
            writer.writerow(
                [
                    restaurant.id,
                    restaurant.name,
                    restaurant.total_sales or 0,  # Manejar valores nulos
                    restaurant.total_revenue or 0.00,  # Manejar valores nulos
                ]
            )
    return file_path
