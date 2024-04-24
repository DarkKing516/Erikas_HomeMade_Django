from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Venta
from .forms import VentaForm

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas:listar_ventas') 
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})
