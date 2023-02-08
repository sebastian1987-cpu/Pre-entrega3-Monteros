from django.db import models
from datetime import datetime

# Create your models here.
class Games1(models.Model):

    nombre = models.CharField(max_length=30)
    plataforma = models.CharField(max_length=30)
    desarrolladora = models.CharField(max_length=40)
    año = models.PositiveIntegerField(blank=True)

class News(models.Model):

    titulo = models.CharField(max_length=30)
    fecha = models.IntegerField()
    genero = models.CharField(max_length=30)

class Inicio1(models.Model):

    portada = models.CharField(max_length=30)
    saludo = models.CharField(max_length=30)
    

class Contacto1(models.Model):

    nombre = models.CharField(max_length=30)
    email= models.CharField(max_length=40)
    
