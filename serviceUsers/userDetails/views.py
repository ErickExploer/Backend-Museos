from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
import json
from django.contrib.auth.models import User



from django.contrib.auth.hashers import make_password


# Crear un nuevo perfil de usuario
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
        
        # Crear el usuario si no existe
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'password': make_password(password),
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

# Obtener un perfil de usuario
@csrf_exempt
def get_user_profile(request, profile_id):
    try:
        profile = UserProfile.objects.get(id=profile_id)
        return JsonResponse({
            'id': profile.id,
            'user': profile.user.username,
            'edad': profile.edad,
            'genero': profile.genero,
            'oficio': profile.oficio
        })
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

# Actualizar un perfil de usuario
@csrf_exempt
def update_user_profile(request, profile_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            profile = UserProfile.objects.get(id=profile_id)
            profile.edad = data.get('edad', profile.edad)
            profile.genero = data.get('genero', profile.genero)
            profile.oficio = data.get('oficio', profile.oficio)
            profile.save()
            return JsonResponse({'message': 'Profile updated successfully'})
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Profile not found'}, status=404)

# Eliminar un perfil de usuario
@csrf_exempt
def delete_user_profile(request, profile_id):
    if request.method == 'DELETE':
        try:
            profile = UserProfile.objects.get(id=profile_id)
            profile.delete()
            return JsonResponse({'message': 'Profile deleted successfully'})
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Profile not found'}, status=404)
