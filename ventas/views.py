from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Venta
from .forms import VentaForm
from pedidos.models import Pedido

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            pedido_id = form.cleaned_data['idPedido'].idPedido  # Obtener el ID del pedido
            pedido = get_object_or_404(Pedido, idPedido=pedido_id)
            venta.subtotal = pedido.subtotal
            venta.iva = pedido.iva
            venta.total = form.cleaned_data['total']  # Usar el total proporcionado en el formulario
            venta.save()
            return redirect('ventas:listar_ventas') 
    else:
        form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})
