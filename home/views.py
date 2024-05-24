from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from reservas.forms import *
from pedidos.models import Producto, TipoProducto, Servicio, TipoServicio
import random

# Create your views here.
# def index(request):
#     return HttpResponse("Pagina principal")

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
    productos = list(Producto.objects.all())
    productos_aleatorios = productos
    if len(productos) >= 1:
        productos_aleatorios = random.sample(productos, min(7, len(productos)))
        tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    else:
        productos_aleatorios = productos
    productos_tamanos = zip(productos_aleatorios, tamanos_imagenes, clase_tamanos_imagenes)
    return render(request, 'index.html', {'productos_aleatorios': productos_aleatorios, 'tamanos_imagenes': tamanos_imagenes, 'form': form, 'productos_tamanos': productos_tamanos})



def catalogo_productos(request):
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()
    tipos_productos = TipoProducto.objects.all()
    tipos_servicios = TipoServicio.objects.all()
    return render(request, 'catalogo.html', {
        'productos': productos,
        'servicios': servicios,
        'tipos_productos': tipos_productos,
        'tipos_servicios': tipos_servicios,
    })