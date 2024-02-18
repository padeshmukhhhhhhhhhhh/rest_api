from rest_framework import serializers
from .models import name

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=name
        fields=['first_name']
