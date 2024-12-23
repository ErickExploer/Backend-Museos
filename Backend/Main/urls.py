from django.contrib import admin

from django.urls import path, include

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include('Usuario.urls')), 
    path('', include('Museos.urls')),  
    path('', include('UsuarioFavoritos.urls')),  
    path('', include('MuseosEventos.urls')),
    path('', include('CartaPresentacion.urls')),
]
