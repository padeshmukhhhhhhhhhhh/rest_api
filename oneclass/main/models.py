from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    