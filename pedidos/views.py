from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            if 'evidencia_pago' in request.FILES:
                pedido.evidencia_pago = request.FILES['evidencia_pago'].read()
            pedido.save()
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