from django.db import models

class Registro():
    Imei = models.ImageField(null=True)
    Modelo = models.CharField(max_length=50, null=False)
    Marca = models.CharField(max_length=50, null=False)
    Rutas = models.IntegerField(null=False)

# Create your models here.
