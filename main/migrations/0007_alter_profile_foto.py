# Generated by Django 5.0.2 on 2024-04-15 21:24

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_profile_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='media/perfil/img/'),
        ),
    ]
