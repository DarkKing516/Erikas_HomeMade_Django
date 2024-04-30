from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm
from django.http import JsonResponse
import base64
import json



def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos, 'uwu': form})




def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form})

def eliminar_pedido(request, pedido_id):
    if request.method == 'DELETE':
        pedido = Pedido.objects.get(idPedido=pedido_id)
        pedido.delete()
        return JsonResponse({'message': 'Pedido eliminado correctamente.'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)