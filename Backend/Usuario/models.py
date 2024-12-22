from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    edad = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], null=True, blank=True)
    oficio = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)  # Correo electrónico único
    password = models.CharField(max_length=228)  # Contraseña (no encriptada)

    def save(self, *args, **kwargs):
        # No encriptamos la contraseña, se guarda tal cual se recibe
        super().save(*args, **kwargs)

    # Propiedad que devuelve el nombre completo del usuario
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.user.username