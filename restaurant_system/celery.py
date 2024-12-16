from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_system.settings")

app = Celery("restaurant_system")

# Configuración desde Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-descubrir tareas
app.autodiscover_tasks()
