from django.shortcuts import render
from rest_framework import viewsets
from .models  import employee
from .serializers import empserializers
# Create your views here.
class emp(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=empserializers
