from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario  # Importa el modelo de usuarios

class TipoServicio(models.Model):
    idTipo_Servicio = models.AutoField(primary_key=True)
    nombre_tipoServicio = models.CharField(max_length=50)
    estado_tipoServicio = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre_tipoServicio

    class Meta:
        db_table = 'tipo_servicios'  # Personalizando el nombre de la tabla

class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True)
    id_TipoServicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    nombre_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    estado_servicio = models.CharField(max_length=1, default='A')
    estado_catalogo = models.CharField(max_length=1, default='A')
    img = models.ImageField(upload_to='servicio_imgs/')  # Ajusta la ruta según tu estructura de carpetas

    def __str__(self):
        return self.nombre_servicio

    class Meta:
        db_table = 'servicios'  # Personalizando el nombre de la tabla

class TipoProducto(models.Model):
    idTipo_Producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    estado_producto = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'tipo_productos'  # Personalizando el nombre de la tabla

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    id_TipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='producto_imgs/')  # Ajusta la ruta según tu estructura de carpetas
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado_producto = models.CharField(max_length=1)
    estado_catalogo = models.CharField(max_length=1)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'  # Personalizando el nombre de la tabla
     

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaCreacion_pedido = models.DateTimeField(default=timezone.now)
    fecha_pedido = models.DateTimeField()
    descripcion_pedido = models.CharField(max_length=255)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    evidencia_pago = models.ImageField(upload_to='pedidos/')
    estado_pedido = models.CharField(max_length=80, default="Por hacer")

    productos = models.ManyToManyField(Producto, through='DetallePedidoProducto')
    servicios = models.ManyToManyField(Servicio, through='DetallePedidoServicio')

    def __str__(self):
        return f"Pedido {self.idPedido}"
    
    class Meta:
        db_table = 'pedidos'  # Personalizando el nombre de la tabla


class DetallePedidoProducto(models.Model):
    idDetalle_Pedido_Productos = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cant_productos = models.IntegerField()
    nombre_productos = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio_inicial_producto = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_productos = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Pedido Producto {self.idDetalle_Pedido_Productos}"

    class Meta:
        db_table = 'detalle_pedido_productos'  # Personalizando el nombre de la tabla

class DetallePedidoServicio(models.Model):
    idDetalle_Pedido_Servicio = models.AutoField(primary_key=True)
    idServicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad_servicios = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    precio_inicial_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_servicios = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Pedido Servicio {self.idDetalle_Pedido_Servicio}"

    class Meta:
        db_table = 'detalle_pedido_servicios' 
