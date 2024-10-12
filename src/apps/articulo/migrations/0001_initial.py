# Generated by Django 5.1.1 on 2024-10-12 01:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Articulo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("titulo", models.CharField(max_length=100)),
                ("contenido", models.TextField()),
                (
                    "fecha_publicada",
                    models.DateField(default=django.utils.timezone.now),
                ),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="articulo.categoria",
                    ),
                ),
            ],
        ),
    ]
