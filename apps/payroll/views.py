from django.shortcuts import render
from rest_framework import viewsets
from .models import Nomina
from .serializers import NominaSerializers

# Create your views here.
class NominaViewsSet(viewsets.ModelViewSet):
    queryset=Nomina.objects.all()
    serializer_class=NominaSerializers