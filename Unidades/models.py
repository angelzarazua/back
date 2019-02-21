from django.db import models
from django.contrib.auth.models import User
from Registro.models import
# Create your models here.

class Unidades(models.Model):
    placa = models.CharField(max_length=25, null=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50, null=False)
    codigoUnico = models.OneToOneField(Resgistro, on_delete=models.CASCADE)
    imei = models.IntegerField(null=False)

