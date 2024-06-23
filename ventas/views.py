from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Venta
from usuarios.models import *
from .forms import VentaForm
from pedidos.models import DetallePedidoProducto, Pedido, DetallePedidoServicio
from django.conf import settings
from django.template.loader import render_to_string
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.utils.text import slugify
from django.utils.html import strip_tags
import pdfkit

def generar_factura_pdf(request, idVenta):
    # Obtiene la venta a partir del idVenta
    venta = get_object_or_404(Venta, idVenta=idVenta)

        # Obtener el pedido asociado a la venta
    pedido = venta.idPedido

    # Obtener los detalles de pedido de productos asociados a este pedido
    detalles_productos = DetallePedidoProducto.objects.filter(idPedido=pedido)
    
    detalles_servicios = DetallePedidoServicio.objects.filter(idPedido=pedido)

    descuento_aumento =  venta.total - venta.idPedido.total


    subtotal_productos = sum(detalle.subtotal_productos for detalle in detalles_productos)

    # Define la ruta al ejecutable de wkhtmltopdf (adaptar según tu instalación)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

        # Aquí genera el contenido HTML de la factura
    contenido_html = render_to_string('ventas/factura_template.html', {
        'venta': venta,
        'pedido': pedido,
        'detalles_productos': detalles_productos,
        'detalles_servicios': detalles_servicios,
        'subtotal_productos': subtotal_productos,
        'descuento_aumento': descuento_aumento,  # Variable calculada

    })

    # Define las opciones para pdfkit
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    # Genera el PDF usando pdfkit
    pdf = pdfkit.from_string(contenido_html, False, configuration=config, options=options)

    # Configura la respuesta HTTP para descargar el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura-{idVenta}.pdf"'

    return response

def listar_ventas(request):
    ventas = Venta.objects.all()
    usuarios = Usuario.objects.all()

    # Obtener parámetros de la URL
    abrir_modal = request.GET.get('abrir_modal', 'false').lower() == 'true'
    pedido_id = request.GET.get('pedido_id', '')

    form = VentaForm()
    return render(request, 'ventas/listar_ventas.html', {
        'ventas': ventas,
        'form': form,
        'usuarios': usuarios,
        'abrir_modal': abrir_modal,
        'pedido_id': pedido_id,
    })

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
    pedidos_vendidos = Venta.objects.values_list('idPedido_id', flat=True)
    pedidos = Pedido.objects.filter(id_Usuario_id=usuario_id).exclude(idPedido__in=pedidos_vendidos)
    pedidos_list = [{'idPedido': pedido.idPedido, 'descripcion': pedido.descripcion_pedido} for pedido in pedidos]
    return JsonResponse({'pedidos': pedidos_list})

def obtener_total_pedido(request, idPedido):
    pedido = Pedido.objects.get(idPedido=idPedido)
    total_pedido = pedido.total
    return JsonResponse({'total_pedido': total_pedido})
