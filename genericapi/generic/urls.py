from django.urls import path
from . import views
urlpatterns = [
    path('second',views.second.as_view(),name="second" ),
    path('',views.index,name="index" )
 
]
