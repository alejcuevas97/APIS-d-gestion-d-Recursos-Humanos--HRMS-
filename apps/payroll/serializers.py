from rest_framework import serializers
from .models import Nomina

class NominaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = ["id","empleado","periodo_inicio","periodo_fin",
                "salario_base","deducciones","bonificaciones","fecha_pago","salario_neto"]

