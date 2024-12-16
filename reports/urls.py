from django.urls import path
from reports.views import GenerateReportView, DownloadReportView

app_name = "reports"

urlpatterns = [
    path("generate/", GenerateReportView.as_view(), name="generate_report"),
    path(
        "download/<str:file_name>/",
        DownloadReportView.as_view(),
        name="download_report",
    ),
]
