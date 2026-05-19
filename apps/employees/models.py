from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento=departamento = models.CharField(max_length=100)
    puesto=models.CharField(max_length=100)
    salario=models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion=models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"