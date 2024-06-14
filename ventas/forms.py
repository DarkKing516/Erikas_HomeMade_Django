from django import forms
from .models import Venta, Pedido

class VentaForm(forms.ModelForm):
    idPedido = forms.ModelChoiceField(queryset=Pedido.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Venta
        fields = ['idPedido', 'metodo_pago', 'descuento', 'total']

    METODO_PAGO_CHOICES = [
        ('nequi', 'Nequi'),
        ('efectivo', 'Efectivo'),
    ]

    metodo_pago = forms.ChoiceField(choices=METODO_PAGO_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'display:block;'}))
    descuento = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'display:block;'}))
    total = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'display:block;'}))
    total_pedido = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    descuento_aumento_type = forms.ChoiceField(
        choices=[('descuento', 'Descuento'), ('aumento', 'Aumento')],
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'descuento_aumento_select'})
    )
    descuento_aumento_value = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'descuento_aumento_input'})
    )