from django.templatetags.static import static
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import os
from django.urls import reverse
from django.shortcuts import redirect
from collections import defaultdict


def crear_pedido_carrito(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        descripcion = request.POST.get('descripcion')
        subtotal = request.POST.get('subtotal')
        iva = request.POST.get('iva')
        total = request.POST.get('total')
        fecha_pedido = request.POST.get('fecha')
        evidencia_pago = request.FILES.get('imagen')

        # Obtener el usuario de la sesión
        usuario_id = request.session.get('usuario_id')

        if usuario_id:
            # Crear y guardar el pedido
            pedido = Pedido(
                id_Usuario_id=usuario_id,
                fecha_pedido=fecha_pedido,
                descripcion_pedido=descripcion,
                subtotal=subtotal,
                iva=iva,
                total=total,
                evidencia_pago=evidencia_pago
            )
            pedido.save()

            # Obtener los productos y servicios del carrito de la sesión
            cart = request.session.get('cart', [])
            grouped_cart = defaultdict(lambda: {'cantidad': 0, 'precio': 0, 'nombre': '', 'descripcion': '', 'tipo': ''})
            for item in cart:
                grouped_cart[item['id']]['cantidad'] += 1
                grouped_cart[item['id']]['precio'] = item['precio']
                grouped_cart[item['id']]['nombre'] = item['nombre']
                grouped_cart[item['id']]['descripcion'] = item['descripcion']
                grouped_cart[item['id']]['tipo'] = item['type']

            for item_id, item_data in grouped_cart.items():
                if item_data['tipo'] == 'producto':
                    producto = Producto.objects.get(idProducto=item_id)
                    if producto.cantidad < item_data['cantidad']:
                        # Si no hay suficiente stock, mostrar un mensaje de error
                        return render(request, 'ver_carrito.html', {'error_message': f'No hay suficiente stock para el producto {producto.nombre}'})

                    else:
                        DetallePedidoProducto.objects.create(
                            idPedido=pedido,
                            idProducto=producto,
                            cant_productos=item_data['cantidad'],
                            nombre_productos=item_data['nombre'],
                            descripcion=item_data['descripcion'],
                            precio_inicial_producto=item_data['precio'],
                            subtotal_productos=item_data['precio'] * item_data['cantidad']
                        )
                        # Restar la cantidad del producto del stock
                        producto.cantidad -= item_data['cantidad']
                        producto.save()
                elif item_data['tipo'] == 'servicio':
                    servicio = Servicio.objects.get(idServicio=item_id)
                    DetallePedidoServicio.objects.create(
                        idPedido=pedido,
                        idServicio=servicio,
                        cantidad_servicios=item_data['cantidad'],
                        descripcion=item_data['descripcion'],
                        precio_inicial_servicio=item_data['precio'],
                        subtotal_servicios=item_data['precio'] * item_data['cantidad']
                    )

            # Limpiar el carrito de la sesión después de crear el pedido
            del request.session['cart']

            # Redirigir a la vista listar_pedidos sin pasar ningún argumento
            return redirect('pedidos:listar_mis_pedidos')
        else:
            # Redirigir al login si no hay usuario en la sesión
            return redirect('usuarios:requestLogin')

    # Renderizar un template si no es POST
    return render(request, 'carrito.html')
def creardetalleServicioPRoducti():

    #crea detales
    return True


def get_image_url(instance, field_name, default_url):
    field = getattr(instance, field_name)
    if field:
        file_path = field.path
        if os.path.exists(file_path):
            return field.url
    return default_url

def count_product_in_cart(cart, product_id):
    count = 0
    for item in cart:
        if item['type'] == 'producto' and item['id'] == product_id:
            count += 1
    return count


def add_to_cart(request):
    if request.method == 'POST' and request.session.get('usuario_id') is not None:
        item_type = request.POST.get('type')
        item_id = request.POST.get('id')
        print(item_id, item_type)
        data = json.loads(request.body)
        item_type = data.get('type')
        item_id = data.get('id')
        print(item_id, item_type)

        default_image_url = '/media/user_images/imagendefectoNoBorrar.gif'

        if not item_type or not item_id:
            return JsonResponse({'success': False, 'message': 'Tipo o ID de artículo no proporcionado.'})

        if 'cart' not in request.session:
            request.session['cart'] = []

        cart = request.session['cart']

        if item_type == 'producto':
            try:
                producto = Producto.objects.get(idProducto=item_id)
                image_url = get_image_url(producto, 'imagen', default_image_url)

                # Contar la cantidad de este producto en el carrito actual
                current_quantity_in_cart = count_product_in_cart(cart, producto.idProducto)

                if current_quantity_in_cart >= producto.cantidad:
                    return JsonResponse({'success': False, 'message': f'No hay suficiente stock de {producto.nombre}.'})
                
                cart.append({
                    'type': 'producto',
                    'id': producto.idProducto,
                    'nombre': producto.nombre,
                    'descripcion': producto.descripcion,
                    'precio': float(producto.precio),
                    # 'imagen': producto.imagen.url if producto.imagen else '/media/user_images/imagendefectoNoBorrar.gif'
                    'imagen': image_url
                })
                request.session['cart'] = cart
                return JsonResponse({'success': True, 'message': f'{producto.nombre} agregado al carrito.'})
            except Producto.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Producto no encontrado.'})

        elif item_type == 'servicio':
            try:
                servicio = Servicio.objects.get(idServicio=item_id)
                image_url = get_image_url(servicio, 'img', default_image_url)

                cart.append({
                    'type': 'servicio',
                    'id': servicio.idServicio,
                    'nombre': servicio.nombre_servicio,
                    'descripcion': servicio.descripcion,
                    'precio': float(servicio.precio_servicio),
                    # 'imagen': servicio.img.url if servicio.img else '/media/user_images/imagendefectoNoBorrar.gif'
                    'imagen': image_url
                })
                request.session['cart'] = cart
                return JsonResponse({'success': True, 'message': f'{servicio.nombre_servicio} agregado al carrito.'})
            except Servicio.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Servicio no encontrado.'})

        else:
            return JsonResponse({'success': False, 'message': 'Tipo de artículo no válido.'})

    return JsonResponse({'success': False, 'message': 'Sesión no iniciada o método no permitido.'})


@require_POST
def remove_cart_item(request):
    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
        
        if not item_id:
            return JsonResponse({'success': False, 'message': 'ID del artículo no proporcionado.'})

        cart = request.session.get('cart', [])
        
        # Encuentra el índice del primer elemento con el ID proporcionado
        index_to_remove = None
        for i, item in enumerate(cart):
            if str(item['id']) == str(item_id):
                index_to_remove = i
                break
        
        if index_to_remove is not None:
            # Elimina el elemento del carrito usando el índice encontrado
            del cart[index_to_remove]
            request.session['cart'] = cart
            request.session.modified = True
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Artículo no encontrado en el carrito.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

def listar_mis_pedidos(request):
    usuario_id = request.session.get('usuario_id')
    default_image_url = '/media/user_images/imagendefectoNoBorrar.gif'

    pedidos = Pedido.objects.filter(id_Usuario_id=usuario_id).exclude(estado_pedido='entregado')

    for pedido in pedidos:
        for detalle_pedido_producto in pedido.detallepedidoproducto_set.all():
            producto = detalle_pedido_producto.idProducto
            # print(f"1 {producto.imagen} \n")
            image_url = get_image_url(producto, 'imagen', default_image_url)
            # print(f"{image_url} \n")
            detalle_pedido_producto.idProducto.imagen = image_url
            # print(f"{detalle_pedido_producto.idProducto.imagen} \n")

        for detalle_pedido_servicio in pedido.detallepedidoservicio_set.all():
            servicio = detalle_pedido_servicio.idServicio
            image_url = get_image_url(servicio, 'img', default_image_url)
            detalle_pedido_servicio.imagen_url = image_url
    # for pedido in pedidos:
    #     for detalle_pedido_producto in pedido.detallepedidoproducto_set.all():
    #         print(f"oaaaaaaaaaa {detalle_pedido_producto.idProducto.imagen} \n")

    return render(request, 'listar_mis_pedidos.html', {'pedidos': pedidos})



def listar_pedidos(request):
    if request.method == 'POST':
        form = CreatePedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save()

            # Obtener los productos y servicios seleccionados
            selected_items = json.loads(request.POST.get('selectedItems', '[]'))

            # Inicializar las variables para los subtotales
            total_precio_productos = 0
            total_precio_servicios = 0

            # Procesar los items seleccionados
            for item in selected_items:
                if item['type'] == 'producto':
                    producto = Producto.objects.get(idProducto=item['id'])
                    quantity = int(item['quantity'])
                    total_precio_productos += producto.precio * quantity
                    descripcion_producto = f"{producto.nombre} ({quantity})"
                    DetallePedidoProducto.objects.create(
                        idProducto=producto,
                        idPedido=pedido,
                        cant_productos=quantity,
                        nombre_productos=producto.nombre,
                        descripcion=descripcion_producto,
                        precio_inicial_producto=producto.precio / 2,
                        subtotal_productos=producto.precio * quantity
                    )
                elif item['type'] == 'servicio':
                    servicio = Servicio.objects.get(idServicio=item['id'])
                    quantity = int(item['quantity'])
                    total_precio_servicios += servicio.precio_servicio * quantity
                    descripcion_servicio = f"{servicio.nombre_servicio} ({quantity})"
                    DetallePedidoServicio.objects.create(
                        idServicio=servicio,
                        idPedido=pedido,
                        cantidad_servicios=quantity,
                        descripcion=descripcion_servicio,
                        precio_inicial_servicio=servicio.precio_servicio / 2,
                        subtotal_servicios=servicio.precio_servicio * quantity
                    )
            return JsonResponse({'success': True, 'message': 'Pedido creada correctamente.'})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        formCreate = CreatePedidoForm()
        pedidos = Pedido.objects.all()
        servicios = Servicio.objects.all()
        productos = Producto.objects.all()
        # Obtener detalles de pedido de productos y servicios para cada pedido
        detalles_productos = DetallePedidoProducto.objects.all()
        detalles_servicios = DetallePedidoServicio.objects.all()

        return render(request, 'listar_pedidos.html', {
            'pedidos': pedidos,
            'servicios': servicios,
            'productos': productos,
            'formCreate': formCreate,
            'detalles_productos': detalles_productos,
            'detalles_servicios': detalles_servicios,
        })


def crear_pedido(request):
    if request.method == 'POST':
        form = CreatePedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save()

            # Obtener los productos y servicios seleccionados
            productos_ids = request.POST.getlist('productos')
            servicios_ids = request.POST.getlist('servicios')

            # Inicializar las variables para los subtotales
            total_precio_productos = 0
            total_precio_servicios = 0

            # Crear detalles de pedido para los productos seleccionados
            for producto_id in productos_ids:
                producto = Producto.objects.get(idProducto=producto_id)
                print(producto)
                total_precio_productos += producto.precio
                descripcion_producto = f"{producto.nombre} (1)"
                DetallePedidoProducto.objects.create(
                    idProducto=producto,
                    idPedido=pedido,
                    cant_productos=1,
                    nombre_productos=producto.nombre,
                    descripcion=descripcion_producto,
                    precio_inicial_producto=producto.precio / 2,
                    subtotal_productos=producto.precio
                )

            # Crear detalles de pedido para los servicios seleccionados
            for servicio_id in servicios_ids:
                servicio = Servicio.objects.get(idServicio=servicio_id)
                total_precio_servicios += servicio.precio_servicio
                descripcion_servicio = f"{servicio.nombre_servicio} (1)"
                DetallePedidoServicio.objects.create(
                    idServicio=servicio,
                    idPedido=pedido,
                    cantidad_servicios=1,
                    descripcion=descripcion_servicio,
                    precio_inicial_servicio=servicio.precio_servicio / 2,
                    subtotal_servicios=servicio.precio_servicio
                )

            return redirect(reverse('pedidos:listar_pedidos'))
    else:
        form = CreatePedidoForm()
        productos = Producto.objects.all()
        servicios = Servicio.objects.all()
    
    context = {
        'form': form,
        'productos': productos,
        'servicios': servicios,
    }
    return render(request, 'listar_pedido.html', context)


@require_POST
def editar_pedido(request):
    pedido_id = request.POST.get('pedido_id')
    print(pedido_id)
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    # Verificar si el estado del pedido es "Por hacer"
    if pedido.estado_pedido != 'Por hacer':
        return JsonResponse({
            'success': False,
            'errors': {'estado_pedido': 'La descripción solo se puede editar si el pedido está en estado "Por hacer".'}
        })

    # Creamos una instancia del formulario con los datos recibidos y la instancia del usuario
    form = PedidoFormEditar(request.POST, instance=pedido)

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
    producto = get_object_or_404(Producto, pk=producto_id)
    imagen_antigua_path = producto.imagen.path  # Guardar la ruta de la imagen antigua

    # Crear una instancia del formulario con los datos recibidos y la instancia del producto
    form = ProductoFormEditarEvidencia(request.POST, request.FILES, instance=producto)

    # Validar el formulario
    if form.is_valid():
        # Guardar los cambios en el producto
        saved_instance = form.save()

        # Eliminar la imagen antigua si se ha subido una nueva
        if 'imagen' in request.FILES:
            if os.path.exists(imagen_antigua_path):
                try:
                    os.remove(imagen_antigua_path)
                except Exception as e:
                    print(f"Error al eliminar la imagen antigua: {e}")

        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolver una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors}) 



@csrf_exempt  # Solo si no tienes el CSRF token configurado correctamente
def eliminar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            print("ID del tipo de producto recibido en el backend:", producto_id)  # Mensaje de depuración
            try:
                producto = Producto.objects.get(pk=producto_id)
                imagen_path = producto.imagen.path
                producto.delete()
                # Eliminar el archivo de imagen
                if os.path.exists(imagen_path):
                    try:
                        os.remove(imagen_path)
                    except Exception as e:
                        print(f"Error al eliminar la imagen: {e}")
                return JsonResponse({'success': True})
            except Producto.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'El producto no existe.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Error en el formato del JSON.'})
    else:
        return JsonResponse({'success': False, 'message': 'Método de solicitud no permitido.'})


@require_POST
def cambiar_estado_productos(request):
    try:
        data = json.loads(request.body)
        producto_id = data.get('producto_id')
        nuevo_estado_producto = data.get('estado_producto')

        producto = Producto.objects.get(pk=producto_id)
        producto.estado_producto = nuevo_estado_producto
        producto.save()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_POST
def cambiar_estado_catalogo(request):
    try:
        data = json.loads(request.body)
        producto_id = data.get('producto_id')
        nuevo_estado_catalogo = data.get('estado_catalogo')

        if nuevo_estado_catalogo not in ['Activo', 'Inactivo']:
            raise ValueError('Estado no válido')

        producto = Producto.objects.get(pk=producto_id)
        producto.estado_catalogo = 'A' if nuevo_estado_catalogo == 'Activo' else 'I'
        producto.save()

        return JsonResponse({'success': True})
    except Producto.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Producto no encontrado'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

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
    
def cambiar_estado_tipo_producto(request):
    if request.method == 'POST':
        tipo_producto_id = request.POST.get('tipo_producto_id')
        print("Tipo Servicio ID:", tipo_producto_id)
        
        data = json.loads(request.body)
        tipo_producto_id = data.get('tipo_producto_id')
        print("Tipo Servicio ID:", tipo_producto_id)
        tipo_producto = TipoProducto.objects.get(pk=tipo_producto_id)
        if tipo_producto.estado_producto == 'Activo':
            tipo_producto.estado_producto = 'Inactivo'
        else:
            tipo_producto.estado_producto = 'Activo'
        tipo_producto.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})


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


def listar_tipo_servicios(request):
    if request.method == 'POST':
        form = TipoServicioForm(request.POST)
        if form.is_valid():
            nombre_tipoServicio = form.cleaned_data['nombre_tipoServicio']
            if TipoServicio.objects.filter(nombre_tipoServicio=nombre_tipoServicio).exists():
                return JsonResponse({'success': False, 'message': 'Nombre Tipo de Servicio ya en uso'})
            
            TServicio = form.save(commit=False)
            TServicio.save()
            return JsonResponse({'success': True})
        else:
            # Si el formulario no es válido, se envían los errores de validación
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        tipo_servicios = TipoServicio.objects.all()
        form = TipoServicioForm()
        return render(request, 'tipo_servicios/listar_tipo_servicio.html', {'tipo_servicios': tipo_servicios, 'form': form})
    
def eliminar_tipo_servicios(request, tipoServicioId):
    print("ID recibido:", tipoServicioId)  # Imprime el ID recibido en la consola
    tipo_servicio = get_object_or_404(TipoServicio, pk=tipoServicioId)
    tipo_servicio.delete()
    return JsonResponse({'message': 'Tipo de Servicio eliminado correctamente'})


@require_POST
def editar_tipo_servicio(request):
    tipoServicioId = request.POST.get('idTipo_Servicio')  # Renombramos la variable aquí
    print("ID del tipo de servicio:", tipoServicioId)

    tipoServicio = get_object_or_404(TipoServicio, pk=tipoServicioId)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del tipoServicio
    form = TipoServicioForm(request.POST, instance=tipoServicio)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en el tipoServicio
        form.save()
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})

def cambiar_estado_tipo_servicio(request):
    if request.method == 'POST':
        tipo_servicio_id = request.POST.get('tipo_servicio_id')
        print("Tipo Servicio ID:", tipo_servicio_id)
        
        data = json.loads(request.body)
        tipo_servicio_id = data.get('tipo_servicio_id')
        print("Tipo Servicio ID:", tipo_servicio_id)
        tipo_servicio = TipoServicio.objects.get(pk=tipo_servicio_id)
        if tipo_servicio.estado_tipoServicio == 'Activo':
            tipo_servicio.estado_tipoServicio = 'Inactivo'
        else:
            tipo_servicio.estado_tipoServicio = 'Activo'
        tipo_servicio.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})
    
    
def listar_servicios(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            nombre_servicio = form.cleaned_data['nombre_servicio']
            if Servicio.objects.filter(nombre_servicio=nombre_servicio).exists():
                return JsonResponse({'success': False, 'message': 'Nombre del servicio ya en uso'})
            
            servicio = form.save(commit=False)
            servicio.save()
            return JsonResponse({'success': True})
        else:
            errors = dict(form.errors.items())
            return JsonResponse({'success': False, 'errors': errors})
    else:
        servicios = Servicio.objects.all()
        tipo_servicios = TipoServicio.objects.all()
        form = ServicioForm()
        return render(request, 'servicios/listar_servicios.html', {'servicios': servicios, 'tipo_servicios': tipo_servicios, 'form': form})
    
    
@require_POST
def editar_servicio(request):
    ServicioId = request.POST.get('idServicio')  # Renombramos la variable aquí
    print("ID del servicio:", ServicioId)

    servicio = get_object_or_404(Servicio, pk=ServicioId)

    # Creamos una instancia del formulario con los datos recibidos y la instancia del Servicio
    form = EditarServicioForm(request.POST, instance=servicio)

    # Validamos el formulario
    if form.is_valid():
        # Guardamos los cambios en el Servicio
        form.save()
        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolvemos una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})
    
@require_POST
def editar_img_servicio(request):
    servicio_id = request.POST.get('idServicio')
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    imagen_antigua_path = servicio.img.path  # Guardar la ruta de la imagen antigua

    # Crear una instancia del formulario con los datos recibidos y la instancia del servicio
    form = ServicioFormEditarImg(request.POST, request.FILES, instance=servicio)

    # Validar el formulario
    if form.is_valid():
        # Guardar los cambios en el servicio
        saved_instance = form.save()

        # Eliminar la imagen antigua si se ha subido una nueva
        if 'img' in request.FILES:
            if os.path.exists(imagen_antigua_path):
                try:
                    os.remove(imagen_antigua_path)
                except Exception as e:
                    print(f"Error al eliminar la imagen antigua: {e}")

        return JsonResponse({'success': True})
    else:
        # Si el formulario no es válido, devolver una respuesta con los errores
        errors = dict(form.errors.items())
        return JsonResponse({'success': False, 'errors': errors})   
    
@csrf_exempt
def eliminar_servicio(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            servicio_id = data.get('servicio_id')
            print("ID del servicio recibido en el backend:", servicio_id)  # Mensaje de depuración
            try:
                servicio = Servicio.objects.get(pk=servicio_id)
                imagen_path = servicio.img.path
                servicio.delete()
                # Eliminar el archivo de imagen
                if os.path.exists(imagen_path):
                    try:
                        os.remove(imagen_path)
                    except Exception as e:
                        print(f"Error al eliminar la imagen: {e}")
                return JsonResponse({'success': True})
            except Servicio.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'El servicio no existe.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Error en el formato del JSON.'})
    else:
        return JsonResponse({'success': False, 'message': 'Método de solicitud no permitido.'})

def cambiar_estado_servicio(request):
    if request.method == 'POST':
        servicio_id = request.POST.get('idServicio')
        print("servicio ID:", servicio_id)
        
        data = json.loads(request.body)
        servicio_id = data.get('idServicio')
        print("servicio ID:", servicio_id)
        servicio = Servicio.objects.get(pk=servicio_id)
        if servicio.estado_servicio == 'A':
            servicio.estado_servicio = 'I'
        else:
            servicio.estado_servicio = 'A'
        servicio.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})
    
    
def cambiar_estado_servicio_catalogo(request):
    if request.method == 'POST':
        servicio_id = request.POST.get('idServicio')
        print("servicio ID:", servicio_id)
        
        data = json.loads(request.body)
        servicio_id = data.get('idServicio')
        print("servicio ID:", servicio_id)
        servicio = Servicio.objects.get(pk=servicio_id)
        if servicio.estado_catalogo == 'A':
            servicio.estado_catalogo = 'I'
        else:
            servicio.estado_catalogo = 'A'
        servicio.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'warning': False})
    
    #------------------------------ detalle producto-----------------------

def listar_detalle_producto(request):
        return render(request, 'ver_carrito.html')
