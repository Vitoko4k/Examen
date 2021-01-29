from django.db import models

# Create your models here.

class Motocicleta(models.Model):
    nombre=models.CharField(max_length=50)
    modelo=models.CharField(max_length=50)
    velocidad=models.CharField(max_length=4)
    cambio=models.CharField(max_length=20)
    precio=models.CharField(max_length=50)

