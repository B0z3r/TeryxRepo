from django.contrib import admin
from .models import Cliente, Persona, Proveedor, Producto, Detalle_Factura, Servicio, Venta, Taller, Detalle_venta, Agenda
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Persona)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle_Factura)
admin.site.register(Servicio)
admin.site.register(Venta)
admin.site.register(Taller)
admin.site.register(Detalle_venta)
admin.site.register(Agenda)