from django.db import models

# Create your models here.
class gurukul(models.Model):
    name=models.CharField(max_length=20)
    vishay=models.CharField(max_length=30)
    guruname=models.CharField(max_length=30)
    dharm=models.CharField(max_length=40)

    