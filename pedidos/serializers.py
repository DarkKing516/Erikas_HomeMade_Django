# pedidos/serializers.py
from rest_framework import serializers
from .models import TipoServicio, Servicio, TipoProducto, Producto, Pedido, DetallePedidoProducto, DetallePedidoServicio

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetallePedidoProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = DetallePedidoProducto
        fields = '__all__'

class DetallePedidoServicioSerializer(serializers.ModelSerializer):
    servicio = ServicioSerializer(read_only=True)

    class Meta:
        model = DetallePedidoServicio
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    detalle_productos = DetallePedidoProductoSerializer(source='detallepedidoproducto_set', many=True, read_only=True)
    detalle_servicios = DetallePedidoServicioSerializer(source='detallepedidoservicio_set', many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def update(self, instance, validated_data):
        estado_pedido = validated_data.pop('estado_pedido', None)
        if estado_pedido is not None:
            instance.estado_pedido = estado_pedido
        return super().update(instance, validated_data)