# Generated by Django 3.1.2 on 2023-11-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='tipo_arreglo',
            field=models.CharField(choices=[('Ajustes básicos', 'Ajustes básicos'), ('Cambio de neumáticos', 'Cambio de neumáticos'), ('Frenos', 'Frenos'), ('Cambio de Cadena, Pedales y Bielas', 'Cambio de Cadena, Pedales y Bielas'), ('Ajuste de Suspensión', 'Ajuste de Suspensión')], max_length=50, verbose_name='Tipo De Arreglo'),
        ),
    ]
