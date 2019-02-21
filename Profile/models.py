from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Addres = models.CharField(max_length=255, null=False)
    Phone = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=50, null=False)
    Edad = models.IntegerField(null=False)
# Create your models here.
