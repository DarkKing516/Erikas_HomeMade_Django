from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
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
from datetime import timedelta, datetime

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
            return JsonResponse({'success': False, 'message': 'Por favor ingrese la fecha valida (que sea dos dias a partir de hoy)', 'errors': errors})
    else:
        reservas = Reserva.objects.all()
        form = ReservaForm()
        return render(request, 'listar_reservas.html', {'reservas': reservas, 'form': form})  

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            fecha_cita = reserva.fecha_cita

            # Redondear la hora al intervalo de media hora más cercano
            minuto = fecha_cita.minute
            if minuto >= 30:
                fecha_cita = fecha_cita.replace(minute=30, second=0, microsecond=0)
            else:
                fecha_cita = fecha_cita.replace(minute=0, second=0, microsecond=0)

            # Verificar si ya existe una reserva en el mismo día y hora
            reservas_existentes = Reserva.objects.filter(fecha_cita=fecha_cita)
            if reservas_existentes.exists():
                return JsonResponse({
                    'success': False,
                    'message': 'Ya existe una reserva para esa fecha y hora.'
                })

            # Guardar la reserva si no hay conflicto
            reserva.fecha_cita = fecha_cita
            reserva.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({
                'success': False,
                'message': 'Por favor ingrese una fecha válida (que sea dos días a partir de hoy)',
                'errors': errors
            })
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})


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
    
@csrf_exempt
def cambiar_fecha_reserva(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        reserva_id = data.get('reserva_id')
        nueva_fecha = data.get('fecha_cita')
        
        try:
            reserva = Reserva.objects.get(pk=reserva_id)
            reserva.fecha_cita = nueva_fecha  # Actualiza la fecha de la cita
            reserva.save()
            
            return JsonResponse({'success': True})
        except Reserva.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Reserva no encontrada'})

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

