from django.shortcuts import render
from rest_framework import viewsets
from .models import Asistencia
from .serializers import AsistenciaSerializers

# Create your views here.
class AsistenciaViewsSet(viewsets.ModelViewSet):
    queryset=Asistencia.objects.all()
    serializer_class=AsistenciaSerializers
