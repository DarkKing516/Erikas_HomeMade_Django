# Generated by Django 5.0.4 on 2024-04-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0011_alter_pedido_evidencia_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='evidencia_pago',
            field=models.ImageField(blank=True, upload_to='evidencia_pago/'),
        ),
    ]
