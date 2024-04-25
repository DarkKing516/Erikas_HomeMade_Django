from django.views.decorators.http import require_http_methods
import requests
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_permisos(request):
    permisos = Permiso.objects.all()
    return render(request, 'permisos/listar_permiso.html', {'permisos': permisos})

def crear_permiso(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_permisos')
    else:
        form = PermisoForm()
    return render(request, 'permisos/crear_permiso.html', {'form': form})

def editar_permiso(request, id_permiso):
    permiso_obj = get_object_or_404(Permiso, pk=id_permiso)  # Changed variable name
    if request.method == 'POST':
        form = PermisoForm(request.POST, instance=permiso_obj)  # Updated variable name here as well
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_permisos')
    else:
        form = PermisoForm(instance=permiso_obj)  # Updated variable name here as well
    return render(request, 'permisos/editar_permiso.html', {'form': form})


def eliminar_permiso(request, id_permiso):
    permiso = get_object_or_404(Permiso, pk=id_permiso)
    permiso.delete()
    return JsonResponse({'message': 'Permiso eliminado correctamente'})


# =================================================================
def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'roles/listar_roles.html', {'roles': roles})

def crear_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_roles')
    else:
        form = RolForm()
    return render(request, 'roles/crear_rol.html', {'form': form})


def editar_rol(request, id_rol):
    rol = get_object_or_404(Rol, pk=id_rol)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_roles')
    else:
        form = RolForm(instance=rol)
    return render(request, 'roles/editar_rol.html', {'form': form})


# def eliminar_rol(request, id_rol):
#     rol = get_object_or_404(Rol, pk=id_rol)
#     try:
#         if request.method == 'POST':
#             rol.delete()
#             return redirect('usuarios:listar_roles')
#         return render(request, 'roles/eliminar_rol.html', {'rol': rol})
#     except PermissionDenied:
#         return render(request, 'roles/error_permiso.html')
def eliminar_rol(request, id_rol):
    rol = get_object_or_404(Rol, pk=id_rol)
    try:
        if request.method == 'POST':
            rol.delete()
            return redirect('usuarios:listar_roles')
        return render(request, 'roles/eliminar_rol.html', {'rol': rol})
    except PermissionDenied:
        # Redirige al usuario a la API de gatos con el código de estado HTTP 403
        response = requests.get('https://http.cat/403')
        image_url = response.url
        return redirect(image_url)


# =================================================================
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuario.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)  # Corrected variable name
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

# def eliminar_usuario(request, id_usuario):
#     usuario = get_object_or_404(Usuario, pk=id_usuario)
#     print("Eliminar usuario llamado")  # Agregar mensaje de registro
#     if request.method == 'POST':
#         usuario.delete()
#         return redirect('usuarios:listar_usuarios')
#     return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

@require_http_methods(["POST", "DELETE"])
def eliminar_usuario(request, id_usuario):
    print("Eliminar usuario llamado")  # Agregar mensaje de registro
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST' or request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message': 'Usuario eliminado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            usuario = authenticate(request, correo=correo, contraseña=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home:index')  # Redirige al dashboard o a la página deseada después del inicio de sesión
            else:
                # Comprobación para mensajes de error específicos
                user_exists = Usuario.objects.filter(correo=correo).exists()
                if user_exists:
                    messages.error(request, 'La contraseña es incorrecta.', extra_tags='contraseña')
                else:
                    messages.error(request, 'El correo electrónico no está registrado.', extra_tags='correo')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})