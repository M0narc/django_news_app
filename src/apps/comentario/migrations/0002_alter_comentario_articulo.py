# Generated by Django 5.1.1 on 2024-10-12 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='articulo.articulo'),
        ),
    ]