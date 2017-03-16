from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):

    perfil = models.OneToOneField(User) # aqui esta nombre, apellido correo y contrase;a 

    def __str__(self):
        return self.perfil.username