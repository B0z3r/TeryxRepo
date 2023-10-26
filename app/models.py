from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre_usuario = models.CharField('Nombre de Usuario', unique=True, max_length=20)
    rut_cliente =  models.IntegerField(primary_key=True, unique=True)
    nombre_cliente = models.CharField(max_length=30)
    apePaterno = models.CharField(max_length=30)
    apeMaterno = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    fono = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.nombre_usuario
    

opciones_consulta = [
        [0,"Administrador"],
        [1,"Vendedor"],
        [2,"Mecanico"]
    ]

class Persona(models.Model):
    nomUsuario = models.CharField(max_length=20, unique=True)
    rut_colaborador = models.IntegerField(primary_key=True, unique=True)
    nombre_completo = models.CharField(max_length=50, unique=True)
    fono = models.IntegerField( unique=True)
    email = models.EmailField( unique=True)
    tipo_perfil = models.IntegerField(choices=opciones_consulta)
    
    def __str__(self):
        return self.nombre_completo


opc_consl_cat = [
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30, unique=True)
    rut_proveedor =  models.IntegerField(unique=True)
    email = models.EmailField( unique=True)
    fono = models.IntegerField( unique=True)
    categoria = models.IntegerField(choices=opc_consl_cat)
    pagina_web = models.URLField(blank=True)

    def __str__(self):
        return self.nombre_proveedor
    

opc_consl_cat = [
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    precio_unitario = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.IntegerField(choices=opc_consl_cat)
    
    def __str__(self):
        return self.nombre_producto

class Detalle_Factura(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    proveedor_id_proveedor = models.ForeignKey(Proveedor, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.cantidad

    
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField()
    tipopago = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion
    
opc_estado = [
        [0,"Listo"],
        [1,"Pendiente"],
        [2,"Atrasado"],
        [3,"En proceso"]
    ]

class Taller(models.Model):
    id_taller = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    nombre_trabajo = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    estado = models.IntegerField(choices=opc_estado)
    modelo_bicicleta = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_servicio
    
class Detalle_venta(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    tipo_servicio = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete = models.PROTECT)
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    cliente_rut_cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    persona_rut_colaborador = models.ForeignKey(Persona, on_delete = models.PROTECT)
    taller_id_taller = models.ForeignKey(Taller, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.tipo_servicio

