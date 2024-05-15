from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST





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

@require_POST
def editar_pedido(request):
    pedido_id = request.POST.get('pedido_id')
    print(pedido_id)
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = PedidoFormEditar(request.POST, instance=pedido)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en la reserva
        saved_instance = form.save()
        print(saved_instance)  # Esta línea imprime la instancia guardada en la consola
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})
    
    
@require_POST
def editar_evidencia_pedido(request):
    pedido_id = request.POST.get('pedido_id')
    print(pedido_id)
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = PedidoFormEditarEvidencia(request.POST, request.FILES, instance=pedido)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en el pedido
        saved_instance = form.save()
        print(saved_instance)  # Esta línea imprime la instancia guardada en la consola
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def eliminar_pedido(request):
    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        print("Pedido ID:", pedido_id)
        data = json.loads(request.body)
        pedido_id = data.get('pedido_id')
        print("Pedido ID:", pedido_id)
        try:
            pedido = Pedido.objects.get(pk=pedido_id)
            if pedido.estado_pedido == 'Entregado':
                return JsonResponse({'success': False, 'message': 'No se puede eliminar el pedido si ya fue entregado'})
            pedido.delete()
            return JsonResponse({'success': True})
        except Pedido.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El pedido no existe'})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})
    
def cambiar_estado(request):
    if request.method == 'POST':
        # Verifica si la solicitud es POST
        
        # Lee los datos del cuerpo de la solicitud JSON
        data = json.loads(request.body)
        
        # Extrae el ID del pedido y el nuevo estado del pedido
        pedido_id = data.get('pedido_id')
        nuevo_estado_pedido = data.get('estado_pedido')
        
        # Imprime los datos para depuración (opcional)
        print("Pedido ID:", pedido_id)
        print("Nuevo estado:", nuevo_estado_pedido)
        
        # Recupera la instancia del pedido de la base de datos utilizando el ID del pedido
        pedido = Pedido.objects.get(pk=pedido_id)
        
        # Actualiza el estado del pedido
        pedido.estado_pedido = nuevo_estado_pedido
        
        # Guarda los cambios en la base de datos
        pedido.save()
        
        # Devuelve una respuesta JSON indicando que la operación fue exitosa
        return JsonResponse({'success': True})
    else:
        # Si la solicitud no es POST, devuelve una respuesta JSON indicando que la operación falló
        return JsonResponse({'success': False})
    

# ----------------------------------------------------------PRODUCTOS--------------------------------------------------------------------------

def listar_productos(request):
    if request.method == 'POST':
        form = CreateProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        formCreate = CreateProductoForm()
        productos = Producto.objects.all()
        return render(request, 'productos/listar_productos.html', {'productos': productos, 'formCreate': formCreate})
    
def crear_producto(request):
    if request.method == 'POST':
        form = CreateProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pedidos:listar_productos')
    else:
        form = CreateProductoForm()
    return render(request, 'crear_producto.html', {'form': form})
    

@require_POST
def editar_productos(request):
    producto_id = request.POST.get('producto_id')
    print(producto_id)
    producto = get_object_or_404(Producto, pk=producto_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = ProductoFormEditar(request.POST, instance=producto)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en la reserva
        saved_instance = form.save()
        print(saved_instance)  # Esta línea imprime la instancia guardada en la consola
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})
    
    
@require_POST
def editar_evidencia_productos(request):
    producto_id = request.POST.get('producto_id')
    print(producto_id)
    producto = get_object_or_404(Pedido, pk=producto_id)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = ProductoFormEditarEvidencia(request.POST, request.FILES, instance=producto_id)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en la reserva
        saved_instance = form.save()
        print(saved_instance)  # Esta línea imprime la instancia guardada en la consola
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

#--------------------------------DESDE AQUI COMIENZA EL CRUD DE TIPO DE PRODCUTO--------------------------------------------


def listar_tipos_productos(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            tipo_producto = form.save(commit=False)
            # Aquí puedes realizar cualquier procesamiento adicional antes de guardar el objeto
            tipo_producto.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'message': 'Hubo un error de validación', 'errors': errors})
    else:
        tipos_productos = TipoProducto.objects.all()
        form = TipoProductoForm()
        return render(request, 'productos/listar_tipo_producto.html', {'tipos_productos': tipos_productos, 'form': form})


def crear_tipo_producto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = TipoProductoForm()
    return render(request, 'productos/crear_tipo_producto.html', {'form': form})

@require_POST
def editar_tipo_producto(request):
    print(request.POST)  # Imprimir el contenido de request.POST
    tipoProductoId = request.POST.get('tipo_producto_id')
    tipo_producto = get_object_or_404(TipoProducto, pk=tipoProductoId)
    
    # Verificar si la solicitud es mediante POST
    if request.method == 'POST':
        # Obtener los datos del formulario y la instancia del tipo de producto
        form = TipoProductoForm(request.POST, instance=tipo_producto)
        
        # Validar el formulario
        if form.is_valid():
            # Guardar los cambios en el tipo de producto
            form.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, devolver una respuesta con los errores
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        # Si la solicitud no es mediante POST, renderizar el formulario para editar el tipo de producto
        form = TipoProductoForm(instance=tipo_producto)
        return render(request, 'editar_tipo_producto.html', {'form': form, 'tipo_producto': tipo_producto})


@require_POST
def eliminar_tipo_producto(request):
    print("Se recibió una solicitud para eliminar un tipo de producto")  # Mensaje de depuración
    if request.method == 'POST':
        try:
            # Cargar los datos JSON de la solicitud
            data = json.loads(request.body)
            tipo_producto_id = data.get('tipo_producto_id')
            print("ID del tipo de producto recibido en el backend:", tipo_producto_id)  # Mensaje de depuración
            tipo_producto = TipoProducto.objects.get(pk=tipo_producto_id)
            tipo_producto.delete()
            return JsonResponse({'success': True})
        except TipoProducto.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El tipo de producto no existe'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido'})

def cambiar_estado_tipo_producto(request):
    if request.method == 'POST':
        tipo_producto_id = request.POST.get('tipo_producto_id')
        
        # Obtener el tipo de producto
        tipo_producto = TipoProducto.objects.get(pk=tipo_producto_id)
        
        # Cambiar el estado del tipo de producto
        if tipo_producto.estado_producto == 'Activo':
            tipo_producto.estado_producto = 'Inactivo'
        else:
            tipo_producto.estado_producto = 'Activo'
        
        # Guardar el cambio
        tipo_producto.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
