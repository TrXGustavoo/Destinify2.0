# Generated by Django 5.0.2 on 2024-03-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0003_remove_lugarturistico_rating_comentario_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
