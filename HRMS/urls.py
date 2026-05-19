from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apps.attendance.views import AsistenciaViewsSet
from apps.departments.views import DepartamentoViewsSet
from apps.employees.views import EmpleadoViewsSet
from apps.payroll.views import NominaViewsSet
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView,SpectacularRedocView


router = routers.DefaultRouter()
router.register(r"empleados", EmpleadoViewsSet)
router.register(r"departamentos", DepartamentoViewsSet)
router.register(r"asistencia", AsistenciaViewsSet)
router.register(r"nomina", NominaViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # Endpoints para documentación y esquema OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('api/v1/', include(router.urls))
    
]
