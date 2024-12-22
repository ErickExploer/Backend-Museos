from django.urls import path
from . import views

urlpatterns = [
    path('favoritos/create', views.create_favorito, name='create_favorito'),
    path('favoritos/read', views.read_favorito, name='read_favorito'),
    path('favoritos/update', views.update_favorito, name='update_favorito'),
    path('favoritos/delete', views.delete_favorito, name='delete_favorito'),
]
