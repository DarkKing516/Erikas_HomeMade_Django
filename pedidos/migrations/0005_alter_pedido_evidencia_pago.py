# Generated by Django 5.0.4 on 2024-08-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_alter_producto_estado_catalogo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='evidencia_pago',
            field=models.ImageField(blank=True, null=True, upload_to='pedidos/'),
        ),
    ]