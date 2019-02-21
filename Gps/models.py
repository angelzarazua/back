from django.db import models
from Registro.models import Registro

class Gps(models.Model):
    Latitud = models.FloatField(null=False)
    Longitud = models.FloatField(null=False)
    Fecha = models.DateField(null=False)
    Imei = models.IntegerField(null=False)
    Dispositivo = models.ForeignKey(Registro,related_name='Dispositivo', on_delete=models.CASCADE)


# Create your models here.
