from django.db import models

class CartaPresentacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    horario = models.CharField(max_length=100)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre