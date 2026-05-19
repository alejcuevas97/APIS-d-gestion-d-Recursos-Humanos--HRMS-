from rest_framework import serializers
from .models import Asistencia

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ["id","empleado","fecha","hora_entrada","hora_salida"]

