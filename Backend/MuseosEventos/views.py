from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento
from Museos.models import Museo  # Asegúrate de importar el modelo Museo
import json











from django.views.decorators.csrf import csrf_exempt

# Crear evento
@csrf_exempt
def create_evento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            museo = Museo.objects.get(id=data['museo_id'])  # Obtener el museo por id
            evento = Evento(
                nombre=data['nombre'],
                fecha=data['fecha'],
                costo=data['costo'],
                museo=museo  # Asignar el museo relacionado
            )
            evento.save()
            return JsonResponse({'message': 'Evento creado exitosamente', 'id': evento.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Campo faltante: {str(e)}'}, status=400)
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo no encontrado'}, status=404)
@csrf_exempt

# Obtener evento
def get_evento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        evento_id = data.get('id')
        if not evento_id:
            return JsonResponse({'error': 'ID requerido'}, status=400)
        try:
            evento = Evento.objects.get(id=evento_id)
            response = {
                'id': evento.id,
                'nombre': evento.nombre,
                'fecha': evento.fecha,
                'costo': evento.costo,
                'museo_id': evento.museo.id,
                'museo_nombre': evento.museo.nombre,
            }
            return JsonResponse(response, status=200)
        except Evento.DoesNotExist:
            return JsonResponse({'error': 'Evento no encontrado'}, status=404)
@csrf_exempt

# Actualizar evento
def update_evento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        evento_id = data.get('id')
        if not evento_id:
            return JsonResponse({'error': 'ID requerido'}, status=400)
        try:
            evento = Evento.objects.get(id=evento_id)
            evento.nombre = data.get('nombre', evento.nombre)
            evento.fecha = data.get('fecha', evento.fecha)
            evento.costo = data.get('costo', evento.costo)
            if 'museo_id' in data:
                museo = Museo.objects.get(id=data['museo_id'])
                evento.museo = museo
            evento.save()
            return JsonResponse({'message': 'Evento actualizado exitosamente'})
        except Evento.DoesNotExist:
            return JsonResponse({'error': 'Evento no encontrado'}, status=404)
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo no encontrado'}, status=404)
@csrf_exempt

# Eliminar evento
def delete_evento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        evento_id = data.get('id')
        if not evento_id:
            return JsonResponse({'error': 'ID requerido'}, status=400)
        try:
            evento = Evento.objects.get(id=evento_id)
            evento.delete()
            return JsonResponse({'message': 'Evento eliminado exitosamente'})
        except Evento.DoesNotExist:
            return JsonResponse({'error': 'Evento no encontrado'}, status=404)
        # Listar todos los eventos de un museo por su ID
@csrf_exempt
def listar_eventos_por_museo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        museo_id = data.get('museo_id')
        
        if not museo_id:
            return JsonResponse({'error': 'Museo ID requerido'}, status=400)

        try:
            museo = Museo.objects.get(id=museo_id)  # Obtener el museo por id
            eventos = Evento.objects.filter(museo=museo)  # Obtener todos los eventos de ese museo

            eventos_data = []
            for evento in eventos:
                eventos_data.append({
                    'id': evento.id,
                    'nombre': evento.nombre,
                    'fecha': evento.fecha,
                    'costo': evento.costo,
                    'museo_id': evento.museo.id,
                    'museo_nombre': evento.museo.nombre
                })

            return JsonResponse({'eventos': eventos_data}, status=200)
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo no encontrado'}, status=404)