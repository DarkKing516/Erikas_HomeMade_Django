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
            try:
                # Obtener el id del pedido desde el formulario
                pedido_id = form.cleaned_data['idPedido'].idPedido  # Usamos idPedido

                # Verificar si ya existe una venta para el pedido dado
                if Venta.objects.filter(idPedido_id=pedido_id).exists():
                    return JsonResponse({'success': False, 'error_type': 'already_exists', 'message': 'Ya existe una venta para este pedido.'}, status=400)

                # Obtener el total actualizado del formulario
                total_final = form.cleaned_data['total']

                # Obtener los valores de descuento/aumento ingresados en el formulario
                descuento_aumento_type = form.cleaned_data['descuento_aumento_type']
                descuento_aumento_value = form.cleaned_data['descuento_aumento_value']

                if total_final < 0:
                    return JsonResponse({'success': False, 'error_type': 'invalid_discount', 'message': 'El descuento no puede resultar en un total negativo.'}, status=400)

                # Crear una instancia de Venta sin guardarla aún
                venta = form.save(commit=False)

                # Buscar y asignar el objeto Pedido correspondiente
                pedido = get_object_or_404(Pedido, idPedido=pedido_id)  # Usamos idPedido
                venta.idPedido = pedido

                # Asignar otros valores necesarios
                venta.subtotal = pedido.subtotal
                venta.iva = pedido.iva
                venta.metodo_pago = form.cleaned_data['metodo_pago']
                venta.descuento = descuento_aumento_value
                venta.total = total_final

                # Guardar la venta
                venta.save()

                # Retorna los datos de la venta creada en formato JSON
                return JsonResponse({'success': True, 'message': 'Venta creada correctamente.'})
            
            except Pedido.DoesNotExist:
                return JsonResponse({'success': False, 'error_type': 'pedido_not_found', 'message': 'El pedido seleccionado no existe.'}, status=404)
            
            except Exception as e:
                # Manejo de excepciones generales
                return JsonResponse({'success': False, 'error_type': 'exception', 'message': str(e)}, status=500)
        
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
