# Generated by Django 4.2.7 on 2023-11-27 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_venta_descripcion_remove_venta_tipo_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='fono',
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Registro'),
        ),
    ]