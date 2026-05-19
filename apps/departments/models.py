from django.db import models

class Departamento(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    descripcion=models.TextField(blank=True)
    gerente=models.ForeignKey("employees.Empleado", on_delete=models.SET_NULL,null=True,blank=True,
                              related_name="departamento_dirigido")
    
    def __str__(self):
        return self.nombre
    