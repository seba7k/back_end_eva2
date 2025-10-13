"""
Configuración de URLs a nivel de proyecto.
Conecta las URLs de las apps y configura el admin y la documentación de la API.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la vista para la documentación de la API (Swagger)
schema_view = get_schema_view(
   openapi.Info(
      title="API Clínica Salud Vital",
      default_version='v1',
      description="Documentación de la API para el sistema de gestión de la Clínica Salud Vital.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contacto@saludvital.cl"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_medica.urls')), # Incluye las URLs de la app
    
    # Rutas para la documentación de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]