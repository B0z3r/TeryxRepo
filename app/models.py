from django.db import models
from datetime import datetime

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
    nomUsuario = models.CharField('Nombre De Usuario', max_length=20, unique=True)
    rut_colaborador = models.IntegerField('Rut Colaborador', primary_key=True, unique=True)
    nombre_completo = models.CharField('Nombre Completo', max_length=50, unique=True)
    fono = models.IntegerField('Teléfono', unique=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    tipo_perfil = models.IntegerField('Tipo De Perfil', choices=opciones_consulta)
    
    def __str__(self):
        return self.nomUsuario


opc_consl_cat = [
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]

class Proveedor(models.Model):
    nombre_proveedor = models.CharField('Nombre del Proveedor', max_length=30, unique=True)
    rut_proveedor =  models.IntegerField('Rut Proveedor', primary_key=True , unique=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    fono = models.IntegerField('Teléfono', unique=True)
    categoria = models.IntegerField('Categoría', choices=opc_consl_cat)
    pagina_web = models.URLField('Página Web', null=True, blank=True)

    def __str__(self):
        return self.nombre_proveedor
    

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
    
    def __str__(self):
        return self.nombre_producto

class Detalle_Factura(models.Model):
    cantidad = models.IntegerField('Cantidad De Productos')
    precio = models.IntegerField('Precio Unitario')
    total = models.IntegerField('Total')
    fecha = models.DateField('Fecha', default=datetime.now)
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    proveedor_rut = models.ForeignKey(Proveedor, on_delete = models.PROTECT)
    
    def __int__(self):
        return self.cantidad
    
opc_estado = [
        [0,"En proceso"],
        [1,"Términado"],
        [2,"Atrasado"]
    ]

opc_estado_pago = [
    [0, "Pendiente"],
    [1, "Pagado"],
]

opciones_arreglo = [
    [('Ajustes básicos','Ajustes básicos')],
    [('Cambio de neumáticos','Cambio de neumáticos')],
    [('Frenos','Frenos')],
    [('Cambio de Cadena, Pedales y Bielas','Cambio de Cadena, Pedales y Bielas')],
    [('Ajuste de Suspensión','Ajuste de Suspensión')]
]

class Taller(models.Model):
    id_taller = models.AutoField('Nº en Taller', primary_key=True)
    fecha_ingreso = models.DateField(' Fecha de Inicio', default=datetime.now)
    fecha_termino = models.DateField('Fecha de Término', default=datetime.now)
    tipo_arreglo = models.CharField('Tipo De Arreglo', max_length=50,choices=[('Ajustes básicos','Ajustes básicos'),('Cambio de neumáticos','Cambio de neumáticos'),('Frenos','Frenos'),('Cambio de Cadena, Pedales y Bielas','Cambio de Cadena, Pedales y Bielas'),('Ajuste de Suspensión','Ajuste de Suspensión')])
    valor = models.IntegerField('Valor')
    descripcion = models.CharField('Descripción', max_length=100)
    estado = models.IntegerField('Estado', choices=opc_estado, default=0)
    modelo_bicicleta = models.CharField('Modelo De Bicicleta', max_length=30)
    estado_pago = models.IntegerField('Estado de Pago', choices=opc_estado_pago, default=0, null=True, blank=True)

    def __str__(self):
        return self.tipo_arreglo
    

class Venta(models.Model):
    id_venta = models.AutoField('Nº Venta', primary_key=True)
    fecha = models.DateField('Fecha', default=datetime.now)
    descripcion = models.CharField('Descipción', max_length=50)
    total = models.IntegerField('Total')
    tipopago = models.CharField('Tipo De Pago', choices=[('EFECTIVO','EFECTIVO'), ('DEBITO', 'DEBITO'), ('CREDITO', 'CREDITO')], max_length=30)
    tipo_servicio = models.CharField('Tipo De Servicio', choices=[('PRODUCTOS','PRODUCTOS'), ('TALLER', 'TALLER')], max_length=30)
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT, null=True, blank=True)
    taller_id_taller = models.ForeignKey(Taller, on_delete = models.PROTECT, null=True, blank=True)
    cliente_rut_cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)

    def __str__(self):
        return self.tipo_servicio
