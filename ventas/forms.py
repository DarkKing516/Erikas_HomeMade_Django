from django import forms
from .models import Venta
from .models import Pedido

class VentaForm(forms.ModelForm):

    idPedido = forms.ModelChoiceField(queryset=Pedido.objects.all(), empty_label=None)

    class Meta:
        model = Venta
        fields = ['idPedido', 'metodo_pago', 'descuento',  'total']

