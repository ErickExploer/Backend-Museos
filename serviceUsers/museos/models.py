from django.db import models
from django.contrib.auth.hashers import make_password

class Museo(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=300)
    descripcion = models.TextField(blank=True)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)  # Campo único para el email
    password = models.CharField(max_length=228)  # Campo para la contraseña encriptada

    def save(self, *args, **kwargs):
        # Encripta la contraseña antes de guardar
        if not self.pk or 'password' in kwargs.get('update_fields', []):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
