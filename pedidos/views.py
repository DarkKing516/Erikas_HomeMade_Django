from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm

def listar_pedidos(request):
    pedidos = Pedido.objects.all()  # Obtener todos los pedidos
    contexto = {'pedidos': pedidos}  # Crear un contexto con los pedidos
    return render(request, 'listar_pedidos.html', contexto)  # Renderizar la plantilla con los datos


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar_pedidos')  # Cambia 'pagina_de_exito' por la URL de la página a la que quieres redirigir después de crear la pedido
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})