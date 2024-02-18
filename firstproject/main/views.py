from django.shortcuts import render
from django.http import JsonResponse
import random
from .models import name
from .serializers import studentserializer
# Create your views here.
def second(request):
    data1=name.objects.all()
    data2=studentserializer(data1,many=True)
    serialized_data = data2.data
    print(type(serialized_data))
    
    data=random.choice(serialized_data)
   
    return JsonResponse(data,safe=False)


def index(request):
    return render(request,"index.html")
