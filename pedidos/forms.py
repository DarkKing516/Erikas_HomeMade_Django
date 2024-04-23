from django import forms
from .models import Pedido, Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
    'idPedido',
    'fecha_pedido',
    'descripcion_pedido',
    'subtotal',
    'iva',
    'total',
    'estado_pedido',
]

