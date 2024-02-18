from django.shortcuts import render
from rest_framework.generics import ListAPIView
from  .serializer import guruserializer
from .models import gurukul
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class search(ListAPIView):
    queryset=gurukul.objects.all()
    serializer_class=guruserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["name"]
