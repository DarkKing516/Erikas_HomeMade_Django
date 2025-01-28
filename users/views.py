from rest_framework import generics, viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import *
from .serializers import *
import requests


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Consumir el endpoint de loginAPI
        api_url = "http://localhost:8000/configuracion/loginAPI/"
        response = requests.post(api_url, json={"email": email, "password": password})
        # api_url = reverse('login_api')
        # full_api_url = request.build_absolute_uri(api_url)
        # response = requests.post(full_api_url, json={"email": email, "password": password})
        if response.status_code == 200:
            data = response.json()
            usuario_id = data.get('usuario_id')
            usuario_nombre = data.get('welcome')

            # Guardar en sesión
            request.session['usuario_id'] = usuario_id
            request.session['usuario_nombre'] = usuario_nombre

            messages.success(request, f"{usuario_nombre}, inicio de sesión exitoso.")
            return redirect('home:home')
        else:
            error_message = response.json().get('error', 'Error desconocido')
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html', {'form': form})



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def profile_image(self, request, pk=None):
        """
        Devuelve la imagen de perfil de un usuario dado su ID.
        """
        try:
            usuario = self.get_object()  # Obtiene el objeto con el ID (pk)
            image_url = usuario.profile_image.url  # Obtener la URL de la imagen de perfil
            return Response({'profile_image': image_url}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def login(request):
    """
    Endpoint para iniciar sesión: recibe correo y contraseña.
    """
    emailRequest = request.data.get('email')
    passwordRequest = request.data.get('password')

    if not emailRequest or not passwordRequest:
        return Response({'error': 'Correo y contraseña son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        usuario = User.objects.get(email=emailRequest)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if check_password(passwordRequest, usuario.password):
        # Aquí puedes devolver un token o cualquier otra información que desees
        return Response({'message': 'Inicio de sesión exitoso', 'welcome': f'¡Bienvenido {usuario.username}!', 'usuario_id': usuario.id}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)