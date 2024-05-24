from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password

from django.views.decorators.http import require_POST
import json
from django.contrib.auth.hashers import make_password  # Importa make_password
from django.views.decorators.http import require_http_methods
import requests
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            
            reserva = form.save(commit=False)
            # Aquí puedes realizar cualquier procesamiento adicional antes de guardar el objeto
            reserva.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'message': 'Hubo un error de validación', 'errors': errors})
    else:
        reservas = Reserva.objects.all()
        form = ReservaForm()
        return render(request, 'listar_reservas.html', {'reservas': reservas, 'form': form})  

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas:listar_reserva') 
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})

# def editar_reserva(request, id_reserva):
#     reserva = get_object_or_404(Reserva, pk=id_reserva)
#     if request.method == 'POST':
#         form = ReservaFormEditar(request.POST, instance=reserva)
#         if form.is_valid():
#             form.save()
#             return redirect('reservas:listar_reserva')
#     else:
#         form = ReservaFormEditar(instance=reserva)
#     return render(request, 'editar_reserva.html', {'form': form})


@require_POST
def editar_reserva(request):
    print(request.POST)  # Imprimir el contenido de request.POST
    reserva_id = request.POST.get('Reserva_id')
    reserva = get_object_or_404(Reserva, pk=reserva_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = ReservaFormEditar(request.POST, instance=reserva)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en la reserva
        saved_instance = form.save()
        print(saved_instance)  # Esta línea imprime la instancia guardada en la consola
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def eliminar_reserva(request):
    if request.method == 'POST':
        reserva_id = request.POST.get('reserva_id')
        print("Usuario ID:", reserva_id)
        data = json.loads(request.body)
        reserva_id = data.get('reserva_id')
        print("Reserva ID:", reserva_id)
        try:
            reserva = Reserva.objects.get(pk=reserva_id)
            
            reserva.delete()
            return JsonResponse({'success': True})
        except Reserva.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'La reserva no existe'})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})


def listar_reservas_cliente(request):
    if not request.session.get('usuario_id'):
        return JsonResponse({'success': False, 'message': 'Usuario no autenticado'}, status=401)

    usuario_id = request.session['usuario_id']

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario_id = usuario_id  # Asigna el usuario a la reserva
            reserva.save()
            return JsonResponse({'success': True})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'message': 'Hubo un error de validación', 'errors': errors})
    else:
        reservas = Reserva.objects.filter(usuario_id=usuario_id)
        form = ReservaForm()
        return render(request, 'mis_reservas.html', {'reservas': reservas, 'form': form})
    
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def cambiar_estado_reserva(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reserva_id = data.get('reserva_id')
        nuevo_estado = data.get('estado')
        
        print("ID de la reserva:", reserva_id)
        print("Nuevo estado:", nuevo_estado)

        reserva = Reserva.objects.get(pk=reserva_id)
        reserva.estado = nuevo_estado
        reserva.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

