# Generated by Django 5.0.4 on 2024-06-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0019_alter_producto_estado_catalogo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(through='pedidos.DetallePedidoProducto', to='pedidos.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='servicios',
            field=models.ManyToManyField(through='pedidos.DetallePedidoServicio', to='pedidos.servicio'),
        ),
    ]
