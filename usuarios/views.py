from django.views.decorators.http import require_POST
import json
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password  # Importa make_password
from django.views.decorators.http import require_http_methods
import requests
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.sessions.models import Session
from .decorators import login_required
from .backends import *
from .models import *
from .forms import *

# Create your views here.
def hello(request):
    if not request.session.get('usuario_id'):
        # Si el usuario no ha iniciado sesión, renderiza la plantilla de "splash screen"
        return render(request, 'splash_screen.html')
    else:
        return HttpResponse("Hello World")


def listar_permisos(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            nombre_permiso = form.cleaned_data['nombre_permiso']
            if Permiso.objects.filter(nombre_permiso=nombre_permiso).exists():
                return JsonResponse({'success': False, 'message': 'Nombre permiso ya en uso'})
            
            permiso = form.save(commit=False)
            permiso.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        permisos = Permiso.objects.all()
        form = PermisoForm()
        return render(request, 'permisos/listar_permiso.html', {'permisos': permisos, 'form': form})

def crear_permiso(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_permisos')
    else:
        form = PermisoForm()
    return render(request, 'permisos/crear_permiso.html', {'form': form})

# def editar_permiso(request, id_permiso):
#     permiso_obj = get_object_or_404(Permiso, pk=id_permiso)  # Changed variable name
#     if request.method == 'POST':
#         form = PermisoForm(request.POST, instance=permiso_obj)  # Updated variable name here as well
#         if form.is_valid():
#             form.save()
#             return redirect('usuarios:listar_permisos')
#     else:
#         form = PermisoForm(instance=permiso_obj)  # Updated variable name here as well
#     return render(request, 'permisos/editar_permiso.html', {'form': form})

@require_POST
def editar_permiso(request):
    permiso_id = request.POST.get('permiso_id')
    permiso = get_object_or_404(Permiso, pk=permiso_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del permiso
    form = PermisoForm(request.POST, instance=permiso)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en el permiso
        form.save()
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def cambiar_estado_permiso(request):
    if request.method == 'POST':
        permiso_id = request.POST.get('permiso_id')
        print("permiso ID:", permiso_id)
        
        data = json.loads(request.body)
        permiso_id = data.get('permiso_id')
        print("permiso ID:", permiso_id)
        permiso = Permiso.objects.get(pk=permiso_id)
        if permiso.estado_permiso == 'A':
            permiso.estado_permiso = 'I'
        else:
            permiso.estado_permiso = 'A'
        permiso.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})
def eliminar_permiso(request, id_permiso):
    permiso = get_object_or_404(Permiso, pk=id_permiso)
    permiso.delete()
    return JsonResponse({'message': 'Permiso eliminado correctamente'})


# =================================================================
# @login_required
def listar_roles(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            nombre_rol = form.cleaned_data['nombre_rol']
            if Rol.objects.filter(nombre_rol=nombre_rol).exists():
                return JsonResponse({'success': False, 'message': 'Nombre del rol ya en uso'})
            
            rol = form.save(commit=False)
            rol.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        roles = Rol.objects.all()
        permisos = Permiso.objects.all()
        form = RolForm()
        return render(request, 'roles/listar_roles.html', {'roles': roles, 'form': form, 'permisos': permisos,})

def crear_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_roles')
    else:
        form = RolForm()
    return render(request, 'roles/crear_rol.html', {'form': form})


# def editar_rol(request, id_rol):
#     rol = get_object_or_404(Rol, pk=id_rol)
#     if request.method == 'POST':
#         form = RolForm(request.POST, instance=rol)
#         if form.is_valid():
#             form.save()
#             return redirect('usuarios:listar_roles')
#     else:
#         form = RolForm(instance=rol)
#     return render(request, 'roles/editar_rol.html', {'form': form})

@require_POST
def editar_rol(request):
    id_rol = request.POST.get('rol_id')
    print(id_rol)
    rol = get_object_or_404(Rol, pk=id_rol)
    form = RolForm(request.POST, instance=rol)
    if form.is_valid():
        form.save()
        if request.session.get('id_rol') == rol.id:
            permisos = list(rol.permisos.values_list('nombre_permiso', flat=True))
            request.session['permisos'] = permisos
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def cambiar_estado_rol(request):
    if request.method == 'POST':
        rol_id = request.POST.get('rol_id')
        print("rol ID:", rol_id)
        
        data = json.loads(request.body)
        rol_id = data.get('rol_id')
        print("rol ID:", rol_id)
        rol = Rol.objects.get(pk=rol_id)
        if rol.estado_rol == 'A':
            rol.estado_rol = 'I'
        else:
            rol.estado_rol = 'A'
        rol.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})
# def eliminar_rol(request, id_rol):
#     rol = get_object_or_404(Rol, pk=id_rol)
#     try:
#         if request.method == 'POST':
#             rol.delete()
#             return redirect('usuarios:listar_roles')
#         return render(request, 'roles/eliminar_rol.html', {'rol': rol})
#     except PermissionDenied:
#         return render(request, 'roles/error_permiso.html')
# def eliminar_rol(request, id_rol):
#     rol = get_object_or_404(Rol, pk=id_rol)
#     try:
#         if request.method == 'POST':
#             rol.delete()
#             return redirect('usuarios:listar_roles')
#         return render(request, 'roles/eliminar_rol.html', {'rol': rol})
#     except PermissionDenied:
#         image_url = 'https://http.cat/403'  # URL de la imagen de gato para el código de estado HTTP 403
#         return JsonResponse({'image_url': image_url})
def eliminar_rol(request, id_rol):
    rol = get_object_or_404(Rol, pk=id_rol)
    if id_rol in [1, 2]:
        image_url = 'https://http.cat/403'  # URL de la imagen de gato para el código de estado HTTP 403
        return JsonResponse({'message': 'No se puede eliminar este rol', 'image_url': image_url}, status=403)
    else:
        rol.delete()
        return JsonResponse({'message': 'Rol eliminado correctamente'})

# =================================================================
def listar_usuarios(request):
    if request.method == 'POST':
        form = CreateUsuario(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            if Usuario.objects.filter(correo=correo).exists():
                return JsonResponse({'success': False, 'message': 'Correo ya en uso'})
            
            usuario = form.save(commit=False)
            usuario.contraseña = make_password(form.cleaned_data['contraseña'])
            usuario.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        formCreate = UsuarioForm()
        formEdit = EditarUsuario()
        usuarios = Usuario.objects.all()
        roles = Rol.objects.all()  # Obtener todos los roles
        return render(request, 'usuarios/listar_usuario.html', {'usuarios': usuarios, 'roles': roles, 'formCreate': formCreate, 'formEdit': formEdit})

def cambiar_rol(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        nuevo_rol_id = request.POST.get('rol_id')
        
        print("Usuario ID:", usuario_id)
        print("Rol ID:", nuevo_rol_id)

        data = json.loads(request.body)
        usuario_id = data.get('usuario_id')
        nuevo_rol_id = data.get('rol_id')
        
        print("Usuario ID:", usuario_id)
        print("Rol ID:", nuevo_rol_id)
        usuario = Usuario.objects.get(pk=usuario_id)
        nuevo_rol = get_object_or_404(Rol, pk=nuevo_rol_id)
        usuario.idRol_id = nuevo_rol_id
        usuario.save()
        # Actualizar la sesión si el usuario cuyo rol se cambia es el usuario autenticado
        if request.session.get('usuario_id') == usuario.id:
            request.session['id_rol'] = nuevo_rol.id
            request.session['rol'] = nuevo_rol.nombre_rol
            # Actualizar los permisos en la sesión
            permisos = list(nuevo_rol.permisos.values_list('nombre_permiso', flat=True))
            request.session['permisos'] = permisos
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def cambiar_estado(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        print("Usuario ID:", usuario_id)
        
        data = json.loads(request.body)
        usuario_id = data.get('usuario_id')
        print("Usuario ID:", usuario_id)
        usuario = Usuario.objects.get(pk=usuario_id)
        if usuario.estado == 'A':
            usuario.estado = 'I'
        else:
            usuario.estado = 'A'
        if request.session.get('estado') == 'A' and usuario_id == request.session.get('usuario_id'):
            usuario.save()
            cerrar_sesion(request)
            return JsonResponse({'success': True})
        usuario.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # Guarda el formulario pero no lo persiste en la base de datos todavía
            usuario.contraseña = make_password(form.cleaned_data['contraseña'])  # Encripta la contraseña antes de guardarla
            usuario.save()  # Ahora guarda el usuario en la base de datos
            return redirect('usuarios:listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})


# def editar_usuario(request, id_usuario):
#     usuario = get_object_or_404(Usuario, pk=id_usuario)
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST, instance=usuario)
#         if form.is_valid():
#             usuario = form.save(commit=False)  # Guarda el formulario pero no lo persiste en la base de datos todavía
#             usuario.contraseña = make_password(form.cleaned_data['contraseña'])  # Encripta la contraseña antes de guardarla
#             usuario.save()  # Ahora guarda el usuario en la base de datos
#             return redirect('usuarios:listar_usuarios')
#     else:
#         form = UsuarioForm(instance=usuario)
#     return render(request, 'usuarios/editar_usuario.html', {'form': form})
# def editar_usuario(request):
#     if request.method == 'POST':
#         usuario_id = request.POST.get('usuario_id')
#         usuario = Usuario.objects.get(id=usuario_id)

#         print("ID del usuario a editar:", usuario_id)
#         data = json.loads(request.body)
#         usuario_id = data.get('usuario_id')
#         print("ID del usuario a editar:", usuario_id)
#         form = EditarUsuario(request.POST, instance=usuario)
#         if form.is_valid():
#             usuario = form.save()
#             # Mensaje de éxito con SweetAlert
#             return JsonResponse({'success': True, 'message': 'Usuario editado correctamente'})
#         else:
#             # Si el formulario no es válido, se envían los errores de validación
#             errors = dict(form.errors.items())
#             return JsonResponse({'success': False, 'errors': errors})
#     else:
#         return redirect('usuarios:listar_usuarios')
@require_POST
def editar_usuario(request):
    usuario_id = request.POST.get('usuario_id')
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = EditarUsuario(request.POST, instance=usuario)

    # Validamos el formulario
    if form.is_valid():
        if usuario_id == 1:
            # Devolvemos un mensaje de error indicando que el usuario no puede ser editado
            return JsonResponse({'success': False, 'errors': 'No se puede editar el rol de este usuario.'})
        
        form.save()
        # Actualizamos los datos de la sesion en caso de que el usuario editado sea el que inició sesion
        if usuario.id == request.session.get('usuario_id'):
            request.session['nombre_usuario'] = usuario.nombre
            request.session['usuario'] = usuario.usuario
            request.session['correo_usuario'] = usuario.correo
            # Si el rol o los permisos del usuario han cambiado, actualizarlos también
            request.session['rol'] = usuario.idRol.nombre_rol
            request.session['id_rol'] = usuario.idRol.id
            permisos = list(usuario.idRol.permisos.values_list('nombre_permiso', flat=True))
            request.session['permisos'] = permisos

        # Guardamos los cambios en el usuario
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})



def editar_usuario_(request, id_usuario):
    if request.session:
        usuario = get_object_or_404(Usuario, pk=id_usuario)
        if request.method == 'POST':
            form = EditarUsuario(request.POST, instance=usuario)
            if form.is_valid():
                usuario = form.save()
                return JsonResponse({'success': True})
            else:
                # Si el formulario no es válido, se envían los errores de validación
                errors = dict(form.errors.items())
                return JsonResponse({'success': False, 'errors': errors})
        else:
            form = EditarUsuario(instance=usuario)
            return render(request, 'usuarios/editar_usuario.html', {'form': form})
# def eliminar_usuario(request, id_usuario):
#     usuario = get_object_or_404(Usuario, pk=id_usuario)
#     print("Eliminar usuario llamado")  # Agregar mensaje de registro
#     if request.method == 'POST':
#         usuario.delete()
#         return redirect('usuarios:listar_usuarios')
#     return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

# @require_http_methods(["POST", "DELETE"])
# def eliminar_usuario(request, id_usuario):
#     print("Eliminar usuario llamado")  # Agregar mensaje de registro
#     usuario = get_object_or_404(Usuario, pk=id_usuario)
#     if request.method == 'POST' or request.method == 'DELETE':
#         usuario.delete()
#         return JsonResponse({'message': 'Usuario eliminado correctamente'})
#     return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_usuario(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        print("Usuario ID:", usuario_id)
        data = json.loads(request.body)
        usuario_id = data.get('usuario_id')
        print("Usuario ID:", usuario_id)
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            if usuario.id == 1:
                return JsonResponse({'success': False, 'message': 'No se puede eliminar el SuperAdmin'})
            if usuario.id == request.session.get('usuario_id'):
                usuario.delete()
                cerrar_sesion(request)
                return JsonResponse({'success': True, 'message': 'Su sesión Será Cerrada'})
            usuario.delete()
            return JsonResponse({'success': True, 'message': 'Usuario Eliminado correctamente.'})
        except Usuario.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El usuario no existe'})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            # Autenticación manual
            backend = CustomBackend()
            usuario = backend.authenticate(request, correo=correo, contraseña=contraseña)
            
            if usuario is not None:
                if usuario.estado != 'A':
                     return JsonResponse({'success': False, 'message': 'Su Cuenta ha sido deshabilitada.'})
                # Obtener el rol del usuario y guardar en la sesión
                request.session['estado'] = usuario.estado
                request.session['rol'] = usuario.idRol.nombre_rol
                request.session['id_rol'] = usuario.idRol.id
                # Obtener los permisos asociados al rol y guardar en la sesión
                permisos = list(usuario.idRol.permisos.values_list('nombre_permiso', flat=True))
                request.session['permisos'] = permisos
                # Establecer manualmente la sesión del usuario
                request.session['usuario_id'] = usuario.id
                request.session['nombre_usuario'] = usuario.nombre
                request.session['usuario'] = usuario.usuario
                request.session['correo_usuario'] = usuario.correo
                # print(request.session)  # Imprimir el contenido de la sesión para depuración
                # print(usuario.nombre)  # Imprime el nombre del usuario en la consola
                # return redirect('home:index')  # Redirige al dashboard o a la página deseada después del inicio de sesión
                print(request.session)  # Imprimir el contenido de la sesión para depuración
                return JsonResponse({'success': True, 'message': f'Bienvenido {usuario.nombre}'})
            else:
                # Comprobación para mensajes de error específicos
                user_exists = Usuario.objects.filter(correo=correo).exists()
                if user_exists:
                    # messages.error(request, 'La contraseña es incorrecta.', extra_tags='contraseña')
                    return JsonResponse({'success': False, 'message': 'La contraseña es incorrecta.'})
                else:
                    # messages.error(request, 'El correo electrónico no está registrado.', extra_tags='correo')
                    return JsonResponse({'success': False, 'message': 'El correo electrónico no está registrado.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def editar_account(request):
    id_usuario = request.session.get('usuario_id')
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            nombre_permiso = form.cleaned_data['nombre_permiso']
            if Permiso.objects.filter(nombre_permiso=nombre_permiso).exists():
                return JsonResponse({'success': False, 'message': 'Nombre permiso ya en uso'})
            
            permiso = form.save(commit=False)
            permiso.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = EditarUsuario(instance=usuario)
        formc = EditarContraseñaUsuario(instance=usuario)
        roles = Rol.objects.all()
        return render(request, 'edit_account.html', {'usuario': usuario, 'roles': roles, 'formc': formc})

def editar_contraseña(request):
    # data = json.loads(request.body)
    # usuario_id = data.get('usuario_id')
    # print("Usuario ID:", usuario_id)
    usuario_id = request.POST.get('usuario_id')
    print("Usuario ID:", usuario_id)
    
    if request.method == 'POST':
        print("Usuario ID:", usuario_id) 
        form = EditarContraseñaUsuario(request.POST)
        if form.is_valid():
            usuario = get_object_or_404(Usuario, pk=usuario_id)
            usuario.contraseña = make_password(form.cleaned_data['contraseña'])  # Encripta la contraseña antes de guardarla
            usuario.save()  # Ahora guarda el usuario en la base de datos
            return JsonResponse({'success': True})
    else:
        editar_account(request)

def cerrar_sesion(request):
    # Eliminar todas las claves de la sesión para cerrarla
    request.session.flush()
    return redirect('usuarios:login')  # Redirige a la página de inicio de sesión

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        correo = request.POST.get('correo')  # Obtén el valor del correo electrónico del POST
        if Usuario.objects.filter(correo=correo).exists():
            return JsonResponse({'success': False, 'message': 'Correo ya en uso'})
        if form.is_valid():
            usuario = form.save(commit=False)
            contraseña = form.cleaned_data['contraseña']
            usuario.contraseña = make_password(contraseña)
            usuario.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, enviar los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def requestLogin(request):
    return render(request, 'splash_screen.html')