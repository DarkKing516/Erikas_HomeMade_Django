from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from reservas.forms import *
from pedidos.models import Producto, TipoProducto
import random

# Create your views here.
# def index(request):
#     return HttpResponse("Pagina principal")

def index(request):
    form = ReservaFormIndex()
    tamanos_imagenes = [
        {'width': 310, 'height': 585},
        {'width': 631, 'height': 587},
        {'width': 311, 'height': 289},
        {'width': 631, 'height': 289},
        {'width': 311, 'height': 289},
        {'width': 311, 'height': 289},
        {'width': 311, 'height': 289},
    ]
    clase_tamanos_imagenes = [
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-8 col-xl-4 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-8 col-xl-4 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop'},
        {'class': 'col-xs-6 col-sm-4 col-xl-2 isotope-item oh-desktop'},
    ]
    # tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    productos = list(Producto.objects.all())
    productos_aleatorios = productos
    if len(productos) >= 1:
        productos_aleatorios = random.sample(productos, min(6, len(productos)))
        tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    else:
        productos_aleatorios = productos
    productos_tamanos = zip(productos_aleatorios, tamanos_imagenes, clase_tamanos_imagenes)
    return render(request, 'index.html', {'productos_aleatorios': productos_aleatorios, 'tamanos_imagenes': tamanos_imagenes, 'form': form, 'productos_tamanos': productos_tamanos})



def catalogo_productos(request):
    productos = Producto.objects.all()
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos, 'tipos_productos': tipos_productos})
