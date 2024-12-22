from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)  # Hacemos que el nombre sea único
    ubicacion = models.CharField(max_length=300)
    descripcion = models.TextField(blank=True)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)  # El correo electrónico ya es único
    password = models.CharField(max_length=228)

    def __str__(self):
        return self.nombre