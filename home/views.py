from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from reservas.forms import *
from pedidos.models import Producto, TipoProducto


# Create your views here.
# def index(request):
#     return HttpResponse("Pagina principal")

def index(request):
    form = ReservaFormIndex()
    return render(request, 'index.html', {'form': form})



def catalogo_productos(request):
    productos = Producto.objects.all()
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos, 'tipos_productos': tipos_productos})
