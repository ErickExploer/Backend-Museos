from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import CartaPresentacion
import json

# Crear una carta de presentación
@csrf_exempt
@require_POST
def crear_carta(request):
    try:
        data = json.loads(request.body)
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')
        calificacion = data.get('calificacion')
        costo = data.get('costo')
        horario = data.get('horario')
        distancia = data.get('distancia')

        if not all([nombre, descripcion, calificacion, costo, horario, distancia]):
            return JsonResponse({"error": "Todos los campos son requeridos."}, status=400)

        carta = CartaPresentacion.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            calificacion=calificacion,
            costo=costo,
            horario=horario,
            distancia=distancia
        )
        return JsonResponse({"message": "Carta de presentación creada con éxito!", "id": carta.id}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Error en el formato JSON."}, status=400)


# Listar todas las cartas de presentación
@csrf_exempt
@require_POST
def listar_cartas(request):
    try:
        cartas = CartaPresentacion.objects.all().values()
        return JsonResponse(list(cartas), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# Obtener una carta de presentación por ID
@csrf_exempt
@require_POST
def obtener_carta(request):
    try:
        data = json.loads(request.body)
        id = data.get('id')

        if not id:
            return JsonResponse({"error": "El campo 'id' es requerido."}, status=400)

        carta = CartaPresentacion.objects.get(id=id)
        return JsonResponse({
            "nombre": carta.nombre,
            "descripcion": carta.descripcion,
            "calificacion": carta.calificacion,
            "costo": carta.costo,
            "horario": carta.horario,
            "distancia": carta.distancia
        })
    
    except CartaPresentacion.DoesNotExist:
        return JsonResponse({"error": "Carta no encontrada."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Error en el formato JSON."}, status=400)


# Editar una carta de presentación
@csrf_exempt
@require_POST
def editar_carta(request):
    try:
        data = json.loads(request.body)
        id = data.get('id')

        if not id:
            return JsonResponse({"error": "El campo 'id' es requerido."}, status=400)

        carta = CartaPresentacion.objects.get(id=id)

        # Actualizamos los campos
        carta.nombre = data.get('nombre', carta.nombre)
        carta.descripcion = data.get('descripcion', carta.descripcion)
        carta.calificacion = data.get('calificacion', carta.calificacion)
        carta.costo = data.get('costo', carta.costo)
        carta.horario = data.get('horario', carta.horario)
        carta.distancia = data.get('distancia', carta.distancia)
        
        carta.save()

        return JsonResponse({"message": "Carta de presentación actualizada con éxito!"})

    except CartaPresentacion.DoesNotExist:
        return JsonResponse({"error": "Carta no encontrada."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Error en el formato JSON."}, status=400)


# Eliminar una carta de presentación
@csrf_exempt
@require_POST
def eliminar_carta(request):
    try:
        data = json.loads(request.body)
        id = data.get('id')

        if not id:
            return JsonResponse({"error": "El campo 'id' es requerido."}, status=400)

        carta = CartaPresentacion.objects.get(id=id)
        carta.delete()

        return JsonResponse({"message": "Carta de presentación eliminada con éxito!"})

    except CartaPresentacion.DoesNotExist:
        return JsonResponse({"error": "Carta no encontrada."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Error en el formato JSON."}, status=400)