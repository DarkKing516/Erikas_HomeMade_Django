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
        'width="310" height="585"',
        'width="310" height="200"',
        'width="310" height="300"',
        'width="310" height="400"',
        'width="310" height="500"',
        'width="310" height="600"',
        'width="310" height="700"',
    ]
    # tamanos_imagenes = tamanos_imagenes[:len(productos_aleatorios)]
    productos = list(Producto.objects.all())
    if len(productos) >= 1:
        productos_aleatorios = random.sample(productos, min(7, len(productos)))
    else:
        productos_aleatorios = productos
    return render(request, 'index.html', {'productos_aleatorios': productos_aleatorios, 'tamanos_imagenes': tamanos_imagenes, 'form': form})



def catalogo_productos(request):
    productos = Producto.objects.all()
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos, 'tipos_productos': tipos_productos})
