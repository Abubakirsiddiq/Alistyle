from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    ism=models.CharField(max_length=55)
    email=models.CharField(max_length=50)
    jins=models.CharField(max_length=30, choices=(("Erkak","Erkak"),("Ayol","Ayol")))
    shahar=models.CharField(max_length=120)
    mamlakat=models.CharField(max_length=75)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

