# Generated by Django 5.0.2 on 2024-04-17 03:01

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_fotoperfil_alter_profile_foto_delete_fotoviagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='geral/img/perfil/'),
        ),
        migrations.DeleteModel(
            name='FotoPerfil',
        ),
    ]