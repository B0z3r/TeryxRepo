# Generated by Django 4.2.7 on 2023-11-15 21:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20231114_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nomUsuario',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Nombre De Usuario'),
        ),
    ]
