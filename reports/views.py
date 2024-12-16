from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reports.tasks import generate_sales_report_task


class GenerateReportView(APIView):
    """
    Endpoint para solicitar la generación de un reporte de ventas
    """

    def post(self, request):
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        if not start_date or not end_date:
            return Response(
                {"error": "start_date y end_date son obligatorios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Llamar a la tarea asíncrona
        task = generate_sales_report_task.delay(start_date, end_date)
        return Response(
            {"task_id": task.id, "message": "Reporte en proceso."},
            status=status.HTTP_202_ACCEPTED,
        )


from django.http import FileResponse
import os


class DownloadReportView(APIView):
    """
    Endpoint para descargar el reporte generado
    """

    def get(self, request, file_name):
        file_path = f"reports/{file_name}"

        if not os.path.exists(file_path):
            return Response(
                {"error": "El reporte no está disponible."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return FileResponse(open(file_path, "rb"), as_attachment=True)
