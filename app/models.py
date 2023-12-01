from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    rut_cliente =  models.IntegerField('Rut', primary_key=True, unique=True)
    nombre_cliente = models.CharField('Nombre ', max_length=30)
    apePaterno = models.CharField('Apellido Paterno', max_length=30)
    apeMaterno = models.CharField('Apellido Materno', max_length=30)
    email = models.EmailField('Correo Electrónico', unique=True)
    fono = models.IntegerField('Teléfono', unique=True)
    
    def __str__(self):
        return self.nombre_cliente
    
opciones_consulta = [
        [0,"Administrador"],
        [1,"Vendedor"],
        [2,"Mecanico"]
    ]

class Persona(models.Model):
    nomUsuario = models.CharField('Nombre De Usuario', max_length=20, unique=True, validators=[MinLengthValidator(5)])
    rut_colaborador = models.IntegerField('Rut Colaborador', primary_key=True, unique=True)
    nombre_completo = models.CharField('Nombre Completo', max_length=50, unique=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    tipo_perfil = models.IntegerField('Tipo De Perfil', choices=opciones_consulta)
    
    def __str__(self):
        return self.nomUsuario
    
    def get_tipo_perfil_display(self):
        return dict(opciones_consulta)[self.tipo_perfil]


opc_consulta_cat = [
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]

class Proveedor(models.Model):
    nombre_proveedor = models.CharField('Nombre del Proveedor', max_length=30, unique=True)
    rut_proveedor =  models.IntegerField('Rut Proveedor', primary_key=True , unique=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    fono = models.IntegerField('Teléfono', unique=True)
    categoria = models.IntegerField('Categoría', choices=opc_consulta_cat)
    pagina_web = models.URLField('Página Web', null=True, blank=True)

    def __str__(self):
        return self.nombre_proveedor
    
    def get_categoria_display(self):
        return dict(opc_consulta_cat)[self.categoria]
    
opc_consl_cat = [
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]

class Producto(models.Model):
    id_producto = models.AutoField('Nº Producto', primary_key=True)
    nombre_producto = models.CharField('Nombre Del Producto', max_length=30)
    marca = models.CharField('Marca', max_length=50)
    descripcion = models.CharField('Descripción', max_length=80)
    precio_unitario = models.IntegerField('Precio Unitario')
    stock = models.IntegerField('Stock')
    categoria = models.IntegerField('Categoría', choices=opc_consl_cat)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha_registro = models.DateField('Fecha de Registro', default=datetime.now)
    
    def __str__(self):
        return self.nombre_producto
    
    def get_categoria_display(self):
        return dict(opc_consl_cat)[self.categoria]
    
    

opc_tipo_arreglo = [
    [0,"Ajustes básicos"],
    [1,"Cambio de neumáticos"],
    [2,"Cambio Frenos"],
    [3,"Reparación de Cadena, Pedales y Bielas"],
    [4,"Ajuste de Suspensión"],
]

opc_estado = [
        [0,"En proceso"],
        [1,"Términado"],
        [2,"Atrasado"],
    ]

opc_estado_pago = [
    [0, "Pendiente"],
    [1, "Pagado"],
]

class Taller(models.Model):
    id_taller = models.AutoField('Nº en Taller', primary_key=True)
    fecha_ingreso = models.DateField('Fecha de Inicio', default=datetime.now)
    fecha_termino = models.DateField('Fecha de Término', default=datetime.now)
    tipo_arreglo = models.IntegerField('Tipo De Arreglo', choices=opc_tipo_arreglo)
    valor = models.IntegerField('Valor')
    descripcion = models.CharField('Descripción', max_length=100)
    estado = models.IntegerField('Estado', choices=opc_estado)
    modelo_bicicleta = models.CharField('Modelo De Bicicleta', max_length=30)
    estado_pago = models.IntegerField('Estado de Pago', choices=opc_estado_pago, null=True, blank=True)
    abono = models.IntegerField('Abono')
    cliente_rut_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id_taller)
    
    def get_estado_display(self):
        return dict(opc_estado)[self.estado]

    def get_estado_pago_display(self):
        return dict(opc_estado_pago)[self.estado_pago]
    
    def get_tipo_arreglo_display(self):
        return dict(opc_tipo_arreglo)[self.tipo_arreglo]
    

class Venta(models.Model):
    id_venta = models.AutoField('Nº Venta', primary_key=True)
    fecha = models.DateField('Fecha', default=datetime.now)
    total = models.IntegerField('Total')
    tipopago = models.CharField('Tipo De Pago', choices=[('EFECTIVO','EFECTIVO'), ('DEBITO', 'DEBITO'), ('CREDITO', 'CREDITO')], max_length=30)
    cantidad_productos_vendidos = models.IntegerField('cantidad de Productos', default=0)
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT, null=True, blank=True)
    taller_id_taller = models.ForeignKey(Taller, on_delete = models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.tipo_servicio

