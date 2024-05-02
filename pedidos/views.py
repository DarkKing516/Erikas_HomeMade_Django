from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm
from django.http import JsonResponse
import base64
import json
from .forms import CreatePedidoForm


def listar_pedidos(request):
    if request.method == 'POST':
        form = CreatePedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        formCreate = CreatePedidoForm()
        pedidos = Pedido.objects.all()
        return render(request, 'listar_pedidos.html', {'pedidos': pedidos, 'formCreate': formCreate})



def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'editar_pedido.html', {'form': form, 'pedido': pedido})

def eliminar_pedido(request, pedido_id):
    if request.method == 'DELETE':
        pedido = Pedido.objects.get(idPedido=pedido_id)
        pedido.delete()
        return JsonResponse({'message': 'Pedido eliminado correctamente.'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)