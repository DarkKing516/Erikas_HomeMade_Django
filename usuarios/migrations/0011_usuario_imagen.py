# Generated by Django 5.0.4 on 2024-05-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='user_images/iconosesion.jpg', upload_to='user_images/'),
        ),
    ]
