from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password, check_password
import json
from .models import UserProfile


# Vista para manejar el login
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Verificar si los datos están presentes
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)
        
        try:
            # Buscar el perfil de usuario por correo electrónico
            user_profile = UserProfile.objects.get(email=email)
            
            # Verificar la contraseña
            if check_password(password, user_profile.user.password):  # Usar check_password para verificar la contraseña encriptada
                # Autenticación exitosa
                return JsonResponse({
                    'message': 'Login successful',
                    'profile_id': user_profile.id,
                    'username': user_profile.user.username,
                    'email': user_profile.user.email,
                    'first_name': user_profile.user.first_name,
                    'last_name': user_profile.user.last_name,
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User profile not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method. Use POST'}, status=405)


# Crear un nuevo perfil de usuario (CREATE)
@csrf_exempt
def create_user_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        edad = data.get('edad')
        genero = data.get('genero')
        oficio = data.get('oficio')

        # Validar que el email no esté vacío
        if not email:
            return JsonResponse({'error': 'Email is required'}, status=400)
        
        # Verificar si el email ya existe en UserProfile
        if UserProfile.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        # Crear el usuario si no existe
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'password': make_password(password),  # Guardar la contraseña de forma segura
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
            }
        )

        if not created:
            return JsonResponse({'error': 'Username already exists'}, status=400)

        # Crear el perfil del usuario
        profile = UserProfile.objects.create(user=user, edad=edad, genero=genero, oficio=oficio)
        
        return JsonResponse({'message': 'Profile and user created successfully', 'profile_id': profile.id}, status=201)


# Obtener un perfil de usuario (GET) pero usamos el POST
@csrf_exempt
def get_user_profile(request):
    if request.method == 'POST':
        try:
            # Cargar el JSON enviado en el cuerpo del POST
            data = json.loads(request.body)
            profile_id = data.get('profile_id')  # Extraer el 'profile_id' del cuerpo

            if not profile_id:
                return JsonResponse({'error': 'Profile ID is required'}, status=400)

            # Obtener el perfil del usuario usando 'profile_id'
            profile = UserProfile.objects.get(id=profile_id)
            user = profile.user  # Relación con la tabla User

            # Retornar todos los datos del perfil y la tabla 'User'
            return JsonResponse({
                'id': profile.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'edad': profile.edad,
                'genero': profile.genero,
                'oficio': profile.oficio
            })
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Profile not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method. Use POST'}, status=405)


# Actualizar un perfil de usuario (UPDATE)
@csrf_exempt
def update_user_profile(request):
    if request.method in ['PUT', 'POST']:  # Acepta tanto PUT como POST
        data = json.loads(request.body)
        profile_id = data.get('profile_id')  # Extraer el 'profile_id' del cuerpo

        if not profile_id:
            return JsonResponse({'error': 'Profile ID is required'}, status=400)

        try:
            # Obtener el perfil del usuario usando 'profile_id'
            profile = UserProfile.objects.get(id=profile_id)

            # Actualizar los campos del perfil
            profile.edad = data.get('edad', profile.edad)
            profile.genero = data.get('genero', profile.genero)
            profile.oficio = data.get('oficio', profile.oficio)

            # Actualizar el 'username' del usuario relacionado (modelo User)
            username = data.get('username')
            if username:
                # Verificar si el username ya existe
                try:
                    profile.user.username = username
                    profile.user.save()
                except IntegrityError:
                    return JsonResponse({'error': 'Username already exists'}, status=400)

            profile.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Profile not found'}, status=404)


# Eliminar un perfil de usuario (DELETE)
@csrf_exempt
def delete_user_profile(request):
    if request.method in ['DELETE', 'POST']:  # Acepta tanto DELETE como POST
        data = json.loads(request.body)
        profile_id = data.get('profile_id')  # Extraer el 'profile_id' del cuerpo

        if not profile_id:
            return JsonResponse({'error': 'Profile ID is required'}, status=400)
        
        try:
            # Obtener el perfil del usuario usando 'profile_id'
            profile = UserProfile.objects.get(id=profile_id)
            user = profile.user  # Obtener el usuario asociado al perfil
            # Eliminar el usuario asociado (si quieres eliminarlo también)
            user.delete()

            # Eliminar el perfil
            profile.delete()

            return JsonResponse({'message': 'Profile deleted successfully'})
        
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Profile not found'}, status=404)