from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/<str:name>', views.go,name="api"),
    path('', views.index,name="index"),
    
]
