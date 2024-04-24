from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reserva
from .forms import *


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas:listar_reserva') 
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})

def editar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, pk=id_reserva)
    if request.method == 'POST':
        form = ReservaFormEditar(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas:listar_reserva')
    else:
        form = ReservaFormEditar(instance=reserva)
    return render(request, 'editar_reserva.html', {'form': form})

def eliminar_reserva(request, id_reserva):
    reserva = get_object_or_404(Reserva, pk=id_reserva)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reservas:listar_reserva')
    return render(request, 'eliminar_reserva.html', {'reserva': reserva})