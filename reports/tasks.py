from celery import shared_task
from reports.utils import generate_sales_report
import os


@shared_task
def generate_sales_report_task(start_date, end_date):
    """
    Tarea asíncrona para generar el reporte de ventas
    """
    file_path = f"reports/sales_report_{start_date}_to_{end_date}.csv"
    if not os.path.exists("reports"):
        os.makedirs("reports")
    return generate_sales_report(start_date, end_date, file_path)
