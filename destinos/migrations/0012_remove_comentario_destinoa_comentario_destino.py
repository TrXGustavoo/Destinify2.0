# Generated by Django 5.0.2 on 2024-06-08 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0011_remove_comentario_destino'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='destinoA',
        ),
        migrations.AddField(
            model_name='comentario',
            name='destino',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_destinos', to='destinos.lugarturistico'),
        ),
    ]