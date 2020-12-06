"Aqui crearemos los modelos de alumnos"
from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_1 = models.CharField(max_length=30)
    apellido_2 = models.CharField(max_length=30,null=True)
    fecha_de_nacimiento = models.DateField(null=True)
    anotaciones = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    midificado = models.DateTimeField(auto_now=True) 
