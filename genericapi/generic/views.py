from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import name
from .serializers import studentserializer
# Create your views here.
class second(ListAPIView):
    queryset=name.objects.all()
    serializer_class= studentserializer

def index(request):
    return render(request,"index.html")    