from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=60)
    autor = models.CharField(max_length=40)
    codigo = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()

class Docente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    asignatura = models.CharField(max_length=40)
