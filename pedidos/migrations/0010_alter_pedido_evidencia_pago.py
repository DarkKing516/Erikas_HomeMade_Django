# Generated by Django 5.0.4 on 2024-04-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_alter_pedido_fechacreacion_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='evidencia_pago',
            field=models.BinaryField(blank=True),
        ),
    ]
