Documentación Técnica - Sistema de Gestión de Pedidos de Restaurantes

1. Objetivo del Proyecto
   El objetivo principal del proyecto es desarrollar un sistema de gestión de pedidos para restaurantes a través de una API RESTful robusta. La solución implementa estándares modernos de desarrollo, seguridad y escalabilidad.

2. Descripción General del Proyecto
   La aplicación permite gestionar:

Restaurantes.
Usuarios autenticados con JWT.
Elementos del menú asociados a restaurantes.
Pedidos y reportes automáticos en CSV.

3. Arquitectura del Proyecto
   La arquitectura está diseñada para garantizar modularidad, escalabilidad, y despliegue eficiente. Los principales componentes son:

Tecnologías Utilizadas
Backend: Django + Django REST Framework (DRF).
Base de Datos: PostgreSQL.
Autenticación: JWT (Simple JWT).
Tareas Asíncronas: Celery con Redis como broker.
Documentación: Swagger UI y ReDoc.
Contenerización: Docker y Docker Compose.
Diagrama de Arquitectura
plaintext
Copiar código
+-----------------------------+
| Cliente |
| (Swagger UI / Postman) |
+-------------+---------------+
|
v
+-------------+---------------+
| API REST (Django) |
| - Autenticación JWT |
| - CRUD para Entidades |
| - Generación de Reportes |
+-------------+---------------+
|
+-------------+---------------+
| PostgreSQL (DB) |
| - Persistencia de datos |
+-------------+---------------+
|
+-------------+---------------+
| Redis (Broker) |
| - Tareas Asíncronas |
+-------------+---------------+
|
+-------------+---------------+
| Celery (Tasks) |
| - Generación de reportes |
| - Carga masiva de datos |
+-----------------------------+

4. Estructura del Proyecto
   El proyecto sigue una estructura modular basada en aplicaciones:

plaintext
Copiar código
restaurant_management/
├── docs/ # Documentación técnica y recursos
├── menu_items/ # Gestión de elementos del menú
│ ├── models.py # Modelos de base de datos
│ ├── serializers.py # Serializadores DRF
│ ├── views.py # Vistas API
│ └── urls.py # Rutas API
├── orders/ # Gestión de pedidos y reportes
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── tasks.py # Tareas asíncronas con Celery
│ └── urls.py
├── restaurants/ # Gestión de restaurantes
├── users/ # Autenticación y usuarios
├── restaurant_system/ # Configuración principal del proyecto
├── docker-compose.yml # Configuración Docker
├── requirements.txt # Dependencias del proyecto
└── README.md # Guía rápida para desarrolladores

5. Configuración del Proyecto
   Requisitos Previos
   Docker y Docker Compose instalados.
   Python 3.9+.
   Pasos de Instalación
   Clonar el repositorio:

bash
Copiar código
git clone https://github.com/tu-usuario/restaurant_management.git
cd restaurant_management
Configurar y ejecutar el proyecto:

bash
Copiar código
docker-compose up --build
Crear las migraciones de base de datos:

bash
Copiar código
docker exec -it restaurant_management-web-1 python manage.py makemigrations
docker exec -it restaurant_management-web-1 python manage.py migrate
Crear un superusuario:

bash
Copiar código
docker exec -it restaurant_management-web-1 python manage.py createsuperuser

6. Endpoints de la API
   Autenticación
   Obtener Token:
   POST /api/token/
   Body: { "username": "91and", "password": "restaurant" }
   Refrescar Token:
   POST /api/token/refresh/
   Gestión de Restaurantes
   Método Endpoint Descripción
   GET /api/restaurants/ Listar restaurantes
   POST /api/restaurants/ Crear un restaurante
   GET /api/restaurants/{id}/ Detalle de restaurante
   PUT /api/restaurants/{id}/ Actualizar restaurante
   DELETE /api/restaurants/{id}/ Eliminar restaurante

7. Generación de Reportes
   Reporte de ventas en CSV con generación asíncrona.
   Ejemplo de tarea en orders/tasks.py:
   python
   Copiar código
   from celery import shared_task
   import csv
   from .models import Order

@shared_task
def generar_reporte_ventas():
with open('reporte_ventas.csv', 'w', newline='') as file:
writer = csv.writer(file)
writer.writerow(['ID', 'Restaurante', 'Total'])
for order in Order.objects.all():
writer.writerow([order.id, order.restaurant.name, order.total])

8. Pruebas y Validación
   Ejecutar Pruebas
   bash
   Copiar código
   docker exec -it restaurant_management-web-1 python manage.py test

9. Documentación de la API
   La documentación se genera automáticamente con drf-yasg:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/ 10. Seguridad
Autenticación: JWT (Simple JWT).
Permisos: IsAuthenticated en endpoints protegidos.
Validación: Serializadores y validaciones personalizadas.

11. Próximos Pasos
    Optimizar consultas con Django ORM.
    Agregar monitoreo y logging con Sentry.
    Mejorar escalabilidad con más workers de Celery.

Contacto
Autor: Andrés Muñoz
Correo: andres.munoz@example.com
Repositorio GitHub: https://github.com/tu-usuario/restaurant_management
