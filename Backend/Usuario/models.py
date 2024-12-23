from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    edad = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], null=True, blank=True)
    oficio = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
