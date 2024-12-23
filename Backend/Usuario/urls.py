from django.urls import path
from . import views

urlpatterns = [
    path('profiles', views.create_user_profile, name='create_user_profile'),  # Crear perfil
    path('profiles/get', views.get_user_profile, name='get_user_profile'),  # Obtener perfil
    path('profiles/update', views.update_user_profile, name='update_user_profile'),  # Actualizar perfil
    path('profiles/delete', views.delete_user_profile, name='delete_user_profile'),  # Eliminar perfil
    path('profiles/all', views.get_all_users, name='get_all_users'),  # Obtener todos los usuarios y perfiles
    path('profiles/login', views.login_user, name='login_user'),  # Login de usuario

]
