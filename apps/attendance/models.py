from django.db import models

# Create your models here.
class Asistencia(models.Model):
    empleado=models.ForeignKey("employees.Empleado", on_delete=models.CASCADE)
    fecha=models.DateField()
    hora_entrada=models.TimeField()
    hora_salida=models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.empleado}-{self.fecha}"