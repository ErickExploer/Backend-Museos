from django.urls import path
from . import views

urlpatterns = [
    path('eventos/create', views.create_evento, name='create_evento'),
    path('eventos/get', views.get_evento, name='get_evento'),
    path('eventos/update', views.update_evento, name='update_evento'),
    path('eventos/delete', views.delete_evento, name='delete_evento'),
    path('eventos/listar_por_museo', views.listar_eventos_por_museo, name='listar_eventos_por_museo'),

]