from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows person to be viewed or edited
    """
    
    queryset = Persona.objects.all().order_by('-id')
    serializer_class = PersonaSerializer
