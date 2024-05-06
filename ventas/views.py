from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Venta
from usuarios.models import *
from .forms import VentaForm
from pedidos.models import Pedido

def listar_ventas(request):
    ventas = Venta.objects.all()
    form = VentaForm()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas,'form': form})

def listar_mis_ventas(request):
    usuario_id = request.session.get('usuario_id')

    # Filtra las ventas por el usuario actual
    ventas = Venta.objects.filter(idPedido__id_Usuario_id=usuario_id)

    return render(request, 'ventas/listar_mis_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)

            # Obtener el total ingresado en el formulario
            total = form.cleaned_data['total']
            
            # Obtener el descuento ingresado en el formulario
            descuento = form.cleaned_data['descuento']
            
            # Calcular el nuevo total después de aplicar el descuento
            total_final = total - descuento

            pedido_id = form.cleaned_data['idPedido'].idPedido
            pedido = get_object_or_404(Pedido, idPedido=pedido_id)
            venta.subtotal = pedido.subtotal
            venta.iva = pedido.iva
            venta.metodo_pago = form.cleaned_data['metodo_pago']
            venta.descuento = form.cleaned_data['descuento']
            venta.total = total_final
            venta.total_pedido = pedido.total  # Establecer el valor del campo total_pedido con el total del pedido seleccionado
            venta.save()
            return redirect('ventas:listar_ventas')
    else:
        if 'idPedido' in request.GET:  # Verificar si se ha proporcionado un ID de pedido en la solicitud
            pedido_id = request.GET['idPedido']
            pedido = get_object_or_404(Pedido, idPedido=pedido_id)
            # Establecer el valor inicial para total_pedido
            initial = {'total_pedido': pedido.total}
            # Crear el formulario con el valor inicial
            form = VentaForm(initial=initial)
            print("Valor inicial de total_pedido:", initial['total_pedido'])  # Agregar esta línea para depuración
        else:
            form = VentaForm()
    return render(request, 'ventas/crear_venta.html', {'form': form})

def obtener_total_pedido(request, idPedido):
    pedido = Pedido.objects.get(idPedido=idPedido)
    total_pedido = pedido.total
    return JsonResponse({'total_pedido': total_pedido})
