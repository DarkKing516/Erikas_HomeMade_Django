# Generated by Django 5.0.4 on 2024-04-19 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_alter_pedido_estado_pedido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='id_Cliente',
        ),
    ]
