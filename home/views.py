from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from reservas.forms import *
from pedidos.models import Producto, TipoProducto, Servicio, TipoServicio
import random
import os
from django.conf import settings
from ventas.models import Venta
from pedidos.models import Pedido, DetallePedidoProducto
from django.db.models import Sum, Count
from django.utils.dateparse import parse_datetime
import json
from datetime import datetime
from django.db.models.functions import TruncMonth

from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth


def dashboard(request):
    # Obtener el año seleccionado del formulario, si está disponible
    selected_year = request.GET.get('year', '')

    # Generar lista de años disponibles, incluyendo 2023
    years = sorted(set(Venta.objects.dates('fecha', 'year').values_list('fecha__year', flat=True)) | {2023})

    # Filtrar ventas y pedidos por año si se selecciona un año
    if selected_year:
        ventas = Venta.objects.filter(fecha__year=selected_year)
        pedidos = Pedido.objects.filter(fecha_pedido__year=selected_year)
    else:
        ventas = Venta.objects.all()
        pedidos = Pedido.objects.all()

    # Agrupar ventas por mes y obtener el conteo de ventas por mes
    ventas_por_mes = ventas.annotate(month=TruncMonth('fecha')).values('month').annotate(total_ventas=Count('idVenta')).order_by('month')

    # Extraer nombres de meses y el conteo de ventas por mes
    ventas_fechas = [venta['month'].strftime('%B') for venta in ventas_por_mes]
    ventas_totales = [venta['total_ventas'] for venta in ventas_por_mes]

    # Completar los meses faltantes con 0 ventas
    meses_completos = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    ventas_por_mes_completas = [0] * 12

    for venta in ventas_por_mes:
        mes = venta['month'].month - 1  # Convertir el mes a índice (0 para Enero, 1 para Febrero, etc.)
        ventas_por_mes_completas[mes] = venta['total_ventas']

    # Obtener los nombres de productos y la cantidad total vendida de cada producto
    if selected_year:
        productos = Producto.objects.filter(detallepedidoproducto__idPedido__fecha_pedido__year=selected_year).annotate(total_vendido=Sum('detallepedidoproducto__cant_productos'))
    else:
        productos = Producto.objects.annotate(total_vendido=Sum('detallepedidoproducto__cant_productos'))

    productos_nombres = list(productos.values_list('nombre', flat=True))
    productos_totales = list(productos.values_list('total_vendido', flat=True))

    # Obtener los nombres de servicios y la cantidad total vendida de cada servicio
    if selected_year:
        servicios = Servicio.objects.filter(detallepedidoservicio__idPedido__fecha_pedido__year=selected_year).annotate(total_vendido=Sum('detallepedidoservicio__cantidad_servicios'))
    else:
        servicios = Servicio.objects.annotate(total_vendido=Sum('detallepedidoservicio__cantidad_servicios'))

    servicios_nombres = list(servicios.values_list('nombre_servicio', flat=True))
    servicios_totales = list(servicios.values_list('total_vendido', flat=True))

    # Obtener los estados de pedidos y contar la cantidad de pedidos en cada estado
    if selected_year:
        pedidos_estados_y_totales = Pedido.objects.filter(fecha_pedido__year=selected_year).values('estado_pedido').annotate(total=Count('idPedido'))
    else:
        pedidos_estados_y_totales = Pedido.objects.values('estado_pedido').annotate(total=Count('idPedido'))

    pedidos_estados = [item['estado_pedido'] for item in pedidos_estados_y_totales]
    pedidos_totales = [item['total'] for item in pedidos_estados_y_totales]

 # Contar los pedidos con estado "Por hacer" con filtro de año, si se aplica
    if selected_year:
        pedidos_por_hacer_count = Pedido.objects.filter(
            estado_pedido='Por hacer',
            fecha_pedido__year=selected_year
        ).count()

        # Obtener los estados de pedidos y contar la cantidad de pedidos en cada estado para el año seleccionado
        pedidos_estados_y_totales = Pedido.objects.filter(
            fecha_pedido__year=selected_year
        ).values('estado_pedido').annotate(total=Count('idPedido'))
    else:
        pedidos_por_hacer_count = Pedido.objects.filter(
            estado_pedido='Por hacer'
        ).count()

        # Obtener los estados de pedidos y contar la cantidad de pedidos en cada estado sin filtro de año
        pedidos_estados_y_totales = Pedido.objects.values('estado_pedido').annotate(total=Count('idPedido'))

    # Agrupar ventas por mes y obtener el total de dinero ganado en cada mes
    ventas_dinero_por_mes = ventas.annotate(month=TruncMonth('fecha')).values('month').annotate(total_dinero=Sum('total')).order_by('month')

    # Extraer el dinero ganado por mes
    ventas_dinero_fechas = [venta['month'].strftime('%B') for venta in ventas_dinero_por_mes]
    ventas_dinero_totales = [venta['total_dinero'] for venta in ventas_dinero_por_mes]

    # Completar los meses faltantes con 0 dinero
    ventas_dinero_por_mes_completas = [0] * 12

    for venta in ventas_dinero_por_mes:
        mes = venta['month'].month - 1  # Convertir el mes a índice (0 para Enero, 1 para Febrero, etc.)
        ventas_dinero_por_mes_completas[mes] = venta['total_dinero']

    context = {
        'ventas_fechas_json': json.dumps(meses_completos, default=str),
        'ventas_totales_json': json.dumps(ventas_por_mes_completas, default=str),
        'productos_nombres_json': json.dumps(productos_nombres, default=str),
        'productos_totales_json': json.dumps(productos_totales, default=str),
        'servicios_nombres_json': json.dumps(servicios_nombres, default=str),
        'servicios_totales_json': json.dumps(servicios_totales, default=str),
        'pedidos_estados_json': json.dumps(pedidos_estados, default=str),
        'pedidos_totales_json': json.dumps(pedidos_totales, default=str),
        'pedidos_por_hacer_count_json': json.dumps(pedidos_por_hacer_count, default=str),
        'ventas_dinero_fechas_json': json.dumps(meses_completos, default=str),  # Usar meses_completos para las etiquetas de meses
        'ventas_dinero_totales_json': json.dumps(ventas_dinero_por_mes_completas, default=str),
        'selected_year': selected_year,
        'years': years  # Lista de años disponibles para el selector, incluyendo 2023
    }

    return render(request, 'dashboard.html', context)


# Create your views here.
# def index(request):
#     return HttpResponse("Pagina principal")

def get_image_url(instance, field_name, default_url):
    field = getattr(instance, field_name)
    if field:
        file_path = field.path
        if os.path.exists(file_path):
            return field.url
    return default_url

def index(request):
    form = ReservaFormIndex()
    tamanos_imagenes = [
        'thumbnail-size-1',
        'thumbnail-size-2',
        'thumbnail-size-3',
        'thumbnail-size-4',
        'thumbnail-size-5',
        'thumbnail-size-6',
        'thumbnail-size-7',
    ]
    # tamanos_imagenes = [
    #     {'width': 310, 'height': 585},
    #     {'width': 631, 'height': 587},
    #     {'width': 311, 'height': 289},
    #     {'width': 631, 'height': 289},
    #     {'width': 311, 'height': 289},
    #     {'width': 311, 'height': 289},
    #     {'width': 311, 'height': 289},
    # ]
    clase_tamanos_imagenes = [
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-2 wow slideInLeft'},
        {'class': 'col-xs-6 col-sm-8 col-xl-4 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-big wow slideInRight'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-2 wow slideInDown'},
        {'class': 'col-xs-6 col-sm-8 col-xl-4 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary wow slideInUp'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-2 wow slideInUp'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-2 wow slideInRight'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop', 'hijo': 'thumbnail thumbnail-mary thumbnail-mary-2 wow slideInLeft'},
    ]
    
    # tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    productos = list(Producto.objects.filter(estado_producto='A', estado_catalogo='A', cantidad__gt=0))
    productos_aleatorios = productos
    if len(productos) >= 1:
        productos_aleatorios = random.sample(productos, min(7, len(productos)))
        tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    else:
        productos_aleatorios = productos
    productos_tamanos = zip(productos_aleatorios, tamanos_imagenes, clase_tamanos_imagenes)
    servicios = list(Servicio.objects.filter(estado_servicio='A', estado_catalogo='A'))
    return render(request, 'index.html', {'productos_aleatorios': productos_aleatorios, 'tamanos_imagenes': tamanos_imagenes, 'form': form, 'productos_tamanos': productos_tamanos, 'servicios': servicios})



def catalogo_productos(request):
    # current_url = request.build_absolute_uri()
    # print(current_url)
    current_path = request.path
    print(current_path)
    default_image_url = '/media/user_images/imagendefectoNoBorrar.gif'

    productos = Producto.objects.filter(estado_producto='A', estado_catalogo='A', cantidad__gt=0)
    servicios = Servicio.objects.filter(estado_servicio='A', estado_catalogo='A')
    tipos_productos = TipoProducto.objects.filter(estado_producto='Activo')
    tipos_servicios = TipoServicio.objects.filter(estado_tipoServicio='Activo')

    # Add image URLs to products and services
    for producto in productos:
        producto.image_url = get_image_url(producto, 'imagen', default_image_url)

    for servicio in servicios:
        servicio.image_url = get_image_url(servicio, 'img', default_image_url)

    return render(request, 'catalogo.html', {
        'productos': productos,
        'servicios': servicios,
        'tipos_productos': tipos_productos,
        'tipos_servicios': tipos_servicios,
    })