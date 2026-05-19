from django.shortcuts import render
from rest_framework import viewsets
from .models import Empleado
from .serializers import EmpleadoSerializers

# Create your views here.
class EmpleadoViewsSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializers