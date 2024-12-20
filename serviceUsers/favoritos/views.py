from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from museos.models import Museo
from .models import Favorito
import json

@csrf_exempt
def create_favorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        usuario_id = data.get('usuario_id')
        museos_ids = data.get('museos', [])

        if not nombre or not usuario_id:
            return JsonResponse({'error': 'Nombre y usuario_id son requeridos'}, status=400)

        try:
            usuario = User.objects.get(id=usuario_id)
            favorito = Favorito.objects.create(nombre=nombre, usuario=usuario)

            # Agregar museos al conjunto de favoritos
            museos = Museo.objects.filter(id__in=museos_ids)
            favorito.museos.set(museos)
            favorito.save()

            return JsonResponse({'message': 'Favorito creado con éxito', 'id': favorito.id}, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

@csrf_exempt
def read_favorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        favorito_id = data.get('id')

        if not favorito_id:
            return JsonResponse({'error': 'ID del favorito es requerido'}, status=400)

        try:
            favorito = Favorito.objects.get(id=favorito_id)
            return JsonResponse({
                'id': favorito.id,
                'nombre': favorito.nombre,
                'usuario': favorito.usuario.username,
                'museos': list(favorito.museos.values('id', 'nombre'))
            })
        except Favorito.DoesNotExist:
            return JsonResponse({'error': 'Favorito no encontrado'}, status=404)

@csrf_exempt
def update_favorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        favorito_id = data.get('id')
        nombre = data.get('nombre')
        museos_ids = data.get('museos', [])

        if not favorito_id:
            return JsonResponse({'error': 'ID del favorito es requerido'}, status=400)

        try:
            favorito = Favorito.objects.get(id=favorito_id)

            if nombre:
                favorito.nombre = nombre

            if museos_ids:
                museos = Museo.objects.filter(id__in=museos_ids)
                favorito.museos.set(museos)

            favorito.save()
            return JsonResponse({'message': 'Favorito actualizado con éxito'})
        except Favorito.DoesNotExist:
            return JsonResponse({'error': 'Favorito no encontrado'}, status=404)

@csrf_exempt
def delete_favorito(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        favorito_id = data.get('id')

        if not favorito_id:
            return JsonResponse({'error': 'ID del favorito es requerido'}, status=400)

        try:
            favorito = Favorito.objects.get(id=favorito_id)
            favorito.delete()
            return JsonResponse({'message': 'Favorito eliminado con éxito'})
        except Favorito.DoesNotExist:
            return JsonResponse({'error': 'Favorito no encontrado'}, status=404)
