from django.urls import path
from . import views

urlpatterns = [
    path('museos/create', views.create_museo, name='create_museo'),
    path('museos/get', views.get_museo, name='get_museo'),
    path('museos/update', views.update_museo, name='update_museo'),
    path('museos/delete', views.delete_museo, name='delete_museo'),
    path('museos/login', views.museo_login, name='museo_login'),  # Ruta de login
    path('museos/all', views.get_all_museos, name='get_all_museos'),  # Obtener todos los museos
]