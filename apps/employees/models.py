from django.db import models

class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    edad=models.IntegerField()
    puesto=models.CharField(max_length=100)
    salario=models.CharField()
    fecha_contratacion=models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"