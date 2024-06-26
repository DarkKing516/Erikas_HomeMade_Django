# Generated by Django 5.0.4 on 2024-04-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('idTipo_Servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipoServicio', models.CharField(max_length=50)),
                ('estado_tipoServicio', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'tipo_servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio_servicio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_servicio', models.CharField(max_length=1)),
                ('estado_catalogo', models.CharField(max_length=1)),
                ('img', models.ImageField(upload_to='servicio_imgs/')),
                ('id_TipoServicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.tiposervicio')),
            ],
            options={
                'db_table': 'servicios',
            },
        ),
    ]
