from django.db import models
from django.contrib.auth.models import User  # Importar el modelo de usuario por defecto de Django
from museos.models import Museo  # Importar el modelo Museo

class Favorito(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre del conjunto de favoritos
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    museos = models.ManyToManyField(Museo, related_name='favoritos')

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"
