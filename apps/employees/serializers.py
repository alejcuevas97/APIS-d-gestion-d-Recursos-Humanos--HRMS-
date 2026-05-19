from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Empleado
        fields= "__all__"
        
        """["id","username","first_name", "last_name","email",
                "departamento","puesto","salario","fecha_contratacion"]"""
        