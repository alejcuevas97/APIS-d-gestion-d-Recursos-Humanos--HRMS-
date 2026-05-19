from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from .models import Nomina
from .serializers import NominaSerializers

@extend_schema_view(
    list=extend_schema(
        summary="Listar Nomina",
        tags=["Nomina"]
    ),
    retrieve=extend_schema(
        summary="Obtener detalle de Nomina",
        tags=["Nomina"]
    ),
    create=extend_schema(
        summary="Crear Nomina",
        tags=["Nomina"]
    ),
    update=extend_schema(
        summary="Actualizar Nomina",
        tags=["Nomina"]
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente Nomina",
        tags=["Nomina"]
    ),
    destroy=extend_schema(
        summary="Eliminar Nomina",
        tags=["Nomina"]
    ),
)
class NominaViewsSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializers
