from django.db import models

class Nomina(models.Model):
    empleado=models.ForeignKey("employees.Empleado", on_delete=models.CASCADE)
    periodo_inicio=models.DateField()
    periodo_fin=models.DateField()
    salario_base=models.DecimalField(max_digits=10, decimal_places=2)
    deducciones=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    bonificaciones=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    fecha_pago=models.DateField()
    
    @property
    def salario_neto(self):
        return self.salario_base - self.deducciones + self.bonificaciones
    
    def __str__(self):
        return f"Nómina {self.empleado} - {self.fecha_pago}"