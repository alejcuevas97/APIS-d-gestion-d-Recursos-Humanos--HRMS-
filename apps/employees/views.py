from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializers

@extend_schema_view(
    list=extend_schema(
        summary="Listar Empleados",
        tags=["Empleados"]
    ),
    retrieve=extend_schema(
        summary="Obtener detalle de Empleados",
        tags=["Empleados"]
    ),
    create=extend_schema(
        summary="Crear Empleados",
        tags=["Empleados"]
    ),
    update=extend_schema(
        summary="Actualizar Empleados",
        tags=["Empleados"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente Empleados",
        tags=["Empleados"]
    ),
    destroy=extend_schema(
        summary="Eliminar Empleados",
        tags=["Empleados"]
    ),
)
class EmpleadoViewsSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializers
