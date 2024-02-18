from django.shortcuts import render
from django.http import JsonResponse
from .serializers import recordserializer
# Create your views here.
from .models import student
def go(request,name):
    data=student.objects.filter(first=name)
    data1=recordserializer(data,many=True)
    serializedata=data1.data
    print(serializedata)
    return JsonResponse(serializedata,safe=False)


def index(request):
    return render(request,"index.html")