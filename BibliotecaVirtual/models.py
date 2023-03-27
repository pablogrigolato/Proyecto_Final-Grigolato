from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=60)
    autor = models.CharField(max_length=40)
    codigo = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Autor: {self.autor} - Codigo: {self.codigo}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Email: {self.email}"

class Docente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()
    asignatura = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - DNI: {self.dni} - Email: {self.email} - Asignatura: {self.asignatura}"
