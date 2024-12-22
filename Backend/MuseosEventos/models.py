from django.db import models
from Museos.models import Museo  # Asegúrate de que el modelo Museo esté importado

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()  # Fecha y hora del evento
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Costo del evento
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)  # Relación con el museo

    def __str__(self):
        return self.nombre