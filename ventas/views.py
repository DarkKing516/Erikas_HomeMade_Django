from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Venta
from usuarios.models import *
from .forms import VentaForm
from pedidos.models import Pedido

def listar_ventas(request):
    ventas = Venta.objects.all()
    usuarios = Usuario.objects.all()

    form = VentaForm()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas,'form': form, 'usuarios': usuarios})

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

            # Obtén el total ingresado en el formulario
            total = form.cleaned_data['total']
            
            # Obtén el descuento ingresado en el formulario
            descuento = form.cleaned_data['descuento']
            
            # Calcular el nuevo total después de aplicar el descuento
            total_final = total - descuento

            # Obtén el ID del Pedido seleccionado desde el formulario
            pedido_id = form.cleaned_data['idPedido'].idPedido
            
            # Busca el objeto Pedido correspondiente
            pedido = get_object_or_404(Pedido, idPedido=pedido_id)
            
            # Asigna los valores necesarios a la venta
            venta.idPedido = pedido
            venta.subtotal = pedido.subtotal
            venta.iva = pedido.iva
            venta.metodo_pago = form.cleaned_data['metodo_pago']
            venta.descuento = form.cleaned_data['descuento']
            venta.total = total_final
            venta.total_pedido = pedido.total
            venta.save()

            # Retorna los datos de la venta creada en formato JSON
            return JsonResponse({'success': True, 'message': 'Venta creada correctamente.'})
        else:
            # Retorna los errores de validación en formato JSON
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'La solicitud no es de tipo POST.'}, status=405)

def obtener_pedidos_usuario(request, usuario_id):
    pedidos = Pedido.objects.filter(id_Usuario_id=usuario_id)
    pedidos_list = [{'idPedido': pedido.idPedido, 'descripcion': pedido.descripcion_pedido} for pedido in pedidos]
    return JsonResponse({'pedidos': pedidos_list})

def obtener_total_pedido(request, idPedido):
    pedido = Pedido.objects.get(idPedido=idPedido)
    total_pedido = pedido.total
    return JsonResponse({'total_pedido': total_pedido})
