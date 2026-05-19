from django.shortcuts import render
from rest_framework import viewsets
from .models import Departamento
from .serializers import DepartamentoSerializers

# Create your views here.
class DepartamentoViewsSet(viewsets.ModelViewSet):
    queryset=Departamento.objects.all()
    serializer_class=DepartamentoSerializers

