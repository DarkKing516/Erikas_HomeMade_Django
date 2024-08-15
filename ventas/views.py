from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, FileResponse
from .models import Venta
from usuarios.models import *
from .forms import VentaForm
from pedidos.models import DetallePedidoProducto, Pedido, DetallePedidoServicio
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.utils.text import slugify
from django.utils.html import strip_tags
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO  # Asegúrate de que esta línea esté incluida


from rest_framework import viewsets
from .serializers import *

def generate_invoice(request, venta_id):
    # Obtener los datos de la venta
    venta = get_object_or_404(Venta, idVenta=venta_id)
    detalles_productos = DetallePedidoProducto.objects.filter(idPedido=venta.idPedido)
    detalles_servicios = DetallePedidoServicio.objects.filter(idPedido=venta.idPedido)

    # Crear un buffer para el PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)

    # Estilos
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(name='Title', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=18, alignment=1, spaceAfter=20)
    style_heading = ParagraphStyle(name='Heading', fontName='Helvetica-Bold', fontSize=14, alignment=1, spaceAfter=12)
    style_normal = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, spaceAfter=6)
    style_table_header = ParagraphStyle(name='TableHeader', fontName='Helvetica-Bold', fontSize=10, alignment=1, spaceAfter=6)
    style_table_data = ParagraphStyle(name='TableData', fontName='Helvetica', fontSize=10, alignment=1)

    # Elementos del PDF
    elements = []

    # Título de la factura
    elements.append(Paragraph("FACTURA DE VENTA", style_title))
    elements.append(Spacer(1, 20))

    # Información del cliente
    elements.append(Paragraph("Información del Cliente", style_heading))
    elements.append(Paragraph(f"Nombre: {venta.idPedido.id_Usuario.nombre}", style_normal))
    elements.append(Paragraph(f"Documento: {venta.idPedido.id_Usuario.documento}", style_normal))
    elements.append(Spacer(1, 10))

    # Información de la venta
    elements.append(Paragraph("Detalles de la Venta", style_heading))
    elements.append(Paragraph(f"Fecha: {venta.fecha.strftime('%d/%m/%Y')}", style_normal))
    elements.append(Paragraph(f"Método de Pago: {venta.metodo_pago}", style_normal))
    elements.append(Paragraph(f"Subtotal: ${venta.subtotal:,.2f}", style_normal))
    elements.append(Paragraph(f"IVA: ${venta.iva:,.2f}", style_normal))
    elements.append(Paragraph(f"Total Pedido: ${venta.idPedido.total:,.2f}", style_normal))
    elements.append(Paragraph(f"Descuento: ${venta.descuento:,.2f}", style_normal))
    elements.append(Paragraph(f"Total Final: ${venta.total:,.2f}", style_heading))
    elements.append(Spacer(1, 20))

    # Tabla de productos
    if detalles_productos.exists():
        elements.append(Paragraph("Productos Vendidos", style_heading))
        product_data = [["Producto", "Cantidad", "Precio Unitario", "Subtotal"]]
        for detalle in detalles_productos:
            product_data.append([
                detalle.nombre_productos,
                str(detalle.cant_productos),
                f"${detalle.precio_inicial_producto:,.2f}",
                f"${detalle.subtotal_productos:,.2f}"
            ])
        table = Table(product_data, colWidths=[250, 80, 90, 100], hAlign='CENTER')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 20))

    # Tabla de servicios
    if detalles_servicios.exists():
        elements.append(Paragraph("Servicios Vendidos", style_heading))
        service_data = [["Servicio", "Cantidad", "Precio Unitario", "Subtotal"]]
        for detalleS in detalles_servicios:
            service_data.append([
                detalleS.idServicio.nombre_servicio,
                str(detalleS.cantidad_servicios),
                f"${detalleS.precio_inicial_servicio:,.2f}",
                f"${detalleS.subtotal_servicios:,.2f}"
            ])
        table = Table(service_data, colWidths=[250, 80, 90, 100], hAlign='CENTER')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 20))

    # Construir el PDF
    doc.build(elements)
    buffer.seek(0)

    # Devolver el archivo como respuesta
    return FileResponse(buffer, as_attachment=True, filename=f'factura_{venta_id}.pdf')


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
    pedidos_list = [{
        'idPedido': pedido.idPedido,
        'fechaCreacion_pedido': pedido.fechaCreacion_pedido.strftime('%Y-%m-%d')  # Ajusta el formato según sea necesario
    } for pedido in pedidos]
    return JsonResponse({'pedidos': pedidos_list})

def obtener_total_pedido(request, idPedido):
    pedido = Pedido.objects.get(idPedido=idPedido)
    total_pedido = pedido.total
    return JsonResponse({'total_pedido': total_pedido})

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer