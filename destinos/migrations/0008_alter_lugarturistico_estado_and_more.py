# Generated by Django 5.0.2 on 2024-06-05 00:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0007_lugarturistico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugarturistico',
            name='estado',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lugarturistico',
            name='foto',
            field=models.ImageField(blank=True, default='static/perfil/img/perfilpadrao.jpg', null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='lugares/'),
        ),
    ]