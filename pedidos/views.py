from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm
from django.http import JsonResponse
import base64


def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            if 'evidencia_pago' in request.FILES:
                evidencia_pago = request.FILES['evidencia_pago']
                try:
                    # Leer el contenido del archivo y codificarlo en base64
                    evidencia_pago_base64 = base64.b64encode(evidencia_pago.read())
                    # Decodificar la cadena base64 y almacenarla como un string
                    pedido.evidencia_pago = evidencia_pago_base64.decode('utf-8')
                    pedido.save()
                    return redirect('listar_pedidos')
                except Exception as e:
                    # Manejar cualquier excepción que pueda ocurrir durante el proceso
                    print("Error al procesar la imagen:", e)
                    # Otra opción es agregar un mensaje de error al formulario y mostrarlo en el template
            else:
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

def eliminar_pedido(request, pedido_id):
    if request.method == 'DELETE':
        pedido = Pedido.objects.get(idPedido=pedido_id)
        pedido.delete()
        return JsonResponse({'message': 'Pedido eliminado correctamente.'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)