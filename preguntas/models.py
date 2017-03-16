from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):

    perfil = models.OneToOneField(User) # aqui esta nombre, apellido correo y contrase;a 

    def __str__(self):
        return self.perfil.username

class Pregunta(models.Model):
	
	nombre = models.CharField(max_length=50)
	clave = models.CharField(max_length=50)
	enunciado = models.TextField()

class Respuesta(models.Model):

	equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
