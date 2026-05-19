from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .models import Departamento
from .serializers import DepartamentoSerializers

@extend_schema_view(
    list=extend_schema(
        summary="Listar Departamento",
        tags=["Departamento"]
    ),
    retrieve=extend_schema(
        summary="Obtener detalle de Departamento",
        tags=["Departamento"]
    ),
    create=extend_schema(
        summary="Crear Departamento",
        tags=["Departamento"]
    ),
    update=extend_schema(
        summary="Actualizar Departamento",
        tags=["Departamento"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente Departamento",
        tags=["Departamento"]
    ),
    destroy=extend_schema(
        summary="Eliminar Departamento",
        tags=["Departamento"]
    ),
)
class DepartamentoViewsSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializers
