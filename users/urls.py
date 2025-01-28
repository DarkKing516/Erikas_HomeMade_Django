from django.conf.urls import *
from django.urls import include, path
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name = 'usuarios'

# Crear un router
router = DefaultRouter()
router.register(r'usuariosAPI', UsuarioViewSet)  # Ruta para los usuarios

urlpatterns = [
    # Rutas para la API de usuarios
    path('', include(router.urls)),
    path('loginAPI/', login, name='login_api'),

    path('catalogo/', lambda request: HttpResponse("¡Hola, mundo!"), name='catalogo'),
    path('dashboard/', lambda request: HttpResponse("¡Hola, mundo!"), name='dashboard'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)