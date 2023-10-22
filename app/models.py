from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut_cliente =  models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=30)
    apePaterno = models.CharField(max_length=30)
    apeMaterno = models.CharField(max_length=30)
    email = models.EmailField()
    fono = models.IntegerField()
    
    def __str__(self):
        return self.nombre_cliente
    

opciones_consulta = [
        [0,"Administrador"],
        [1,"Vendedor"],
        [2,"Mecanico"]
    ]


class Persona(models.Model):
    rut_usuario = models.IntegerField(primary_key=True)
    contrasenna = models.CharField(max_length=30)
    nombre_completo = models.CharField(max_length=50)
    fono = models.IntegerField()
    email = models.EmailField()
    tipo_perfil = models.IntegerField(choices=opciones_consulta)
    
    def __str__(self):
        return self.nombre_completo


class Proveedor(models.Model):
    rut_proveedor =  models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30)
    email = models.EmailField()
    fono = models.IntegerField()
    categoria = models.CharField(max_length=50)
    pagina_web = models.URLField()

    def __str__(self):
        return self.nombre_proveedor
    

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80)
    precio_unitario = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_producto

class Detalle_Factura(models.Model):
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()
    proveedor_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    proveedor_rut = models.ForeignKey(Proveedor, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.cantidad

class Servicio(models.Model):
    tipo_servicio = models.CharField(max_length=30)
    detalle = models.CharField(max_length=50)
    fecha = models.DateField()
    persona_rut = models.ForeignKey(Persona, on_delete = models.PROTECT)
    cliente_rut = models.ForeignKey(Cliente, on_delete = models.PROTECT)

    def __str__(self):
        return self.tipo_servicio
    
class Venta(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField()
    tipopago = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion
    
class Taller(models.Model):
    nombre_trabajo = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)
    fecha = models.DateField
    servicio_id_servicio = models.ForeignKey(Servicio, on_delete = models.PROTECT)

    def __str__(self):
        return self.nombre_servicio
    
class Detalle_venta(models.Model):
    cantidad = models.IntegerField()
    venta_id_venta = models.ForeignKey(Venta, on_delete = models.PROTECT)
    producto_id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    servicio_id_servicio = models.ForeignKey(Servicio, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.cantidad
    
class Agenda(models.Model):
    fecha_ingreso = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    descripcion = models.TextField(max_length=100)
    modelo_bici = models.CharField(max_length=30)
    taller_id_taller = models.ForeignKey(Taller, on_delete = models.PROTECT)
    
    def __str__(self):
        return self.fecha_ingreso
    

