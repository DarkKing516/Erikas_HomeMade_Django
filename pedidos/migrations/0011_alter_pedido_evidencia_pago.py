# Generated by Django 5.0.4 on 2024-04-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_alter_pedido_evidencia_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='evidencia_pago',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]