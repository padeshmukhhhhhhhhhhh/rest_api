from django.db import models

# Create your models here.
class student(models.Model):
    first=models.CharField(max_length=255,    null=True)
    last=models.CharField(max_length=255, null=True)
    address=models.TextField(null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)

 