# Generated by Django 3.1.2 on 2023-10-25 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre_usuario', models.CharField(max_length=20)),
                ('rut_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=30)),
                ('apePaterno', models.CharField(max_length=30)),
                ('apeMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('tipo_servicio', models.IntegerField()),
                ('cliente_rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nomUsuario', models.CharField(max_length=20)),
                ('rut_colaborador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('fono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('tipo_perfil', models.IntegerField(choices=[[0, 'Administrador'], [1, 'Vendedor'], [2, 'Mecanico']])),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('precio_unitario', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.IntegerField(choices=[[0, 'Indumentaria'], [1, 'Accesorio'], [2, 'Repuestos']])),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fono', models.IntegerField()),
                ('categoria', models.IntegerField()),
                ('pagina_web', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('tipopago', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_trabajo', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=30)),
                ('detalle_venta_detalle_venta_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.detalle_venta')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='persona_id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.persona'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='producto_id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='venta_id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta'),
        ),
        migrations.CreateModel(
            name='Detalle_Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
                ('proveedor_id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto')),
                ('proveedor_rut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('descripcion', models.TextField(max_length=100)),
                ('taller_id_taller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.taller')),
            ],
        ),
    ]
