# Generated by Django 4.2.7 on 2023-11-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_persona_fono_alter_producto_fecha_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad_productos_vendidos',
            field=models.IntegerField(default=0, verbose_name='cantidad de Productos'),
        ),
    ]