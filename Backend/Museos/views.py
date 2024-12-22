from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Museo
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse

@csrf_exempt
def museo_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Verificar que el email y la contraseña no estén vacíos
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        try:
            # Buscar el museo por email
            museo = Museo.objects.get(email=email)

            # Verificar la contraseña
            if check_password(password, museo.password):
                return JsonResponse({
                    'message': 'Login successful',
                    'id': museo.id,
                    'nombre': museo.nombre,
                    'ubicacion': museo.ubicacion,
                    'telefono': museo.telefono,
                    'email': museo.email
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museum not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method. Use POST'}, status=405)










@csrf_exempt
def create_museo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            museo = Museo(
                nombre=data['nombre'],
                ubicacion=data['ubicacion'],
                descripcion=data.get('descripcion', ''),
                horario_apertura=data['horario_apertura'],
                horario_cierre=data['horario_cierre'],
                telefono=data.get('telefono', ''),
                email=data['email'],
                password=make_password(data['password'])
            )
            museo.save()
            return JsonResponse({'message': 'Museo created successfully', 'id': museo.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)

@csrf_exempt
def get_museo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        museo_id = data.get('id')
        if not museo_id:
            return JsonResponse({'error': 'ID is required'}, status=400)
        try:
            museo = Museo.objects.get(id=museo_id)
            response = {
                'id': museo.id,
                'nombre': museo.nombre,
                'ubicacion': museo.ubicacion,
                'descripcion': museo.descripcion,
                'horario_apertura': museo.horario_apertura.strftime('%H:%M'),
                'horario_cierre': museo.horario_cierre.strftime('%H:%M'),
                'telefono': museo.telefono,
                'email': museo.email
            }
            return JsonResponse(response, status=200)
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo not found'}, status=404)

@csrf_exempt
def update_museo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        museo_id = data.get('id')
        if not museo_id:
            return JsonResponse({'error': 'ID is required'}, status=400)
        try:
            museo = Museo.objects.get(id=museo_id)
            museo.nombre = data.get('nombre', museo.nombre)
            museo.ubicacion = data.get('ubicacion', museo.ubicacion)
            museo.descripcion = data.get('descripcion', museo.descripcion)
            museo.horario_apertura = data.get('horario_apertura', museo.horario_apertura)
            museo.horario_cierre = data.get('horario_cierre', museo.horario_cierre)
            museo.telefono = data.get('telefono', museo.telefono)
            museo.email = data.get('email', museo.email)
            if 'password' in data:
                museo.password = make_password(data['password'])
            museo.save()
            return JsonResponse({'message': 'Museo updated successfully'})
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo not found'}, status=404)

@csrf_exempt
def delete_museo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        museo_id = data.get('id')
        if not museo_id:
            return JsonResponse({'error': 'ID is required'}, status=400)
        try:
            museo = Museo.objects.get(id=museo_id)
            museo.delete()
            return JsonResponse({'message': 'Museo deleted successfully'})
        except Museo.DoesNotExist:
            return JsonResponse({'error': 'Museo not found'}, status=404)
