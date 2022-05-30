from django.db import models

# Create your models here.


class Tema(models.Model):
    nombre = models.CharField(max_length=40)
    duracion = models.FloatField()
    añoLanzamiento = models.IntegerField()
    autor = models.CharField(max_length=50)


class Musico(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)


class Banda(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
