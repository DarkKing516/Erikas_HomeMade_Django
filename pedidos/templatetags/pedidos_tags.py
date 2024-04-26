from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def get_pedido_url(pedido):
    return reverse('editar_pedido', args=[pedido.idPedido])