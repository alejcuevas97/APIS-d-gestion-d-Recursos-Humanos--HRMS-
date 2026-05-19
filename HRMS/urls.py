from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from apps.attendance.views import AsistenciaViewsSet
from apps.departments.views import DepartamentoViewsSet
from apps.employees.views import EmpleadoViewsSet
from apps.payroll.views import NominaViewsSet

router = routers.DefaultRouter()
router.register(r"empleados", EmpleadoViewsSet)
router.register(r"departamentos", DepartamentoViewsSet)
router.register(r"asistencia", AsistenciaViewsSet)
router.register(r"nomina", NominaViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
