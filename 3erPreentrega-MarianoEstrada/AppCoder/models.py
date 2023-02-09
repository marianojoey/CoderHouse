from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=30)  #indica que va a tomar una variable de tipo texto
    camada=models.IntegerField()   #indica que va a tomar una variable de tipo entero.
    
class Profesor(models.Model):
    legajo=models.IntegerField()
    nombre_apellido=models.CharField(max_length=60)
    email=models.EmailField(max_length=30)
    curso_dictado=models.CharField(max_length=30)

class Estudiante(models.Model):
    legajo=models.IntegerField()
    nombre_apellido=models.CharField(max_length=60)
    email=models.EmailField(max_length=30)
    cursando=models.CharField(max_length=30)
    camada=models.IntegerField()
    