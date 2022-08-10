from django.db import models


class Bolim(models.Model):
    nom=models.CharField(max_length=100)
    rasm=models.FileField(blank=True)


class Ichki(models.Model):
    nom=models.CharField(max_length=100)
    rasm=models.FileField()
    bolim=models.ForeignKey(Bolim,on_delete=models.CASCADE)


class Mahsulot(models.Model):
    nom=models.CharField(max_length=100)
    narx=models.IntegerField()
    ishlabchiqaruvchi=models.CharField(max_length=100)
    olchov=models.CharField(max_length=70, blank=True)
    min_buyurtma=models.CharField(max_length=75, blank=True)
    kafolat=models.CharField(max_length=100)
    yetkazish=models.CharField(max_length=100)
    mavjud=models.BooleanField()
    batafsil=models.TextField()
    ichki=models.ForeignKey(Ichki,on_delete=models.CASCADE)


class Media(models.Model):
    rasm=models.FileField()
    mahsulot=models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name="ichki_mahsulot")

