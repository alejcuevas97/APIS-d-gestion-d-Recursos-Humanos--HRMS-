from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    #esto debo agregar para poder enrutar 
    default_auto_field='django.db.models.BigAutoField'
    name = 'apps.employees'
