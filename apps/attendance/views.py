from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .models import Asistencia
from .serializers import AsistenciaSerializers

@extend_schema_view(
    list=extend_schema(
        summary="Listar Asistencias",
        tags=["Asistencias"]
    ),
    retrieve=extend_schema(
        summary="Obtener detalle de Asistencias",
        tags=["Asistencias"]
    ),
    create=extend_schema(
        summary="Crear Asistencias",
        tags=["Asistencias"]
    ),
    update=extend_schema(
        summary="Actualizar Asistencias",
        tags=["Asistencias"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente Asistencias",
        tags=["Asistencias"]
    ),
    destroy=extend_schema(
        summary="Eliminar Asistencias",
        tags=["Asistencias"]
    ),
)
class AsistenciaViewsSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializers
