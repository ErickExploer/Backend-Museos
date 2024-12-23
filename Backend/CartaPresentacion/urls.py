from django.urls import path
from . import views

urlpatterns = [
    path('CartaPresentacion/create', views.crear_carta, name='crear_carta'),
    path('CartaPresentacion/listar', views.listar_cartas, name='listar_cartas'),
    path('CartaPresentacion/obtener', views.obtener_carta, name='obtener_carta'),
    path('CartaPresentacion/editar', views.editar_carta, name='editar_carta'),
    path('CartaPresentacion/eliminar', views.eliminar_carta, name='eliminar_carta'),
]