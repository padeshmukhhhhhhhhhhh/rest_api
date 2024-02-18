from .models import gurukul
from rest_framework import serializers

class guruserializer(serializers.ModelSerializer):
    class   Meta:
        model=gurukul
        fields="__all__"