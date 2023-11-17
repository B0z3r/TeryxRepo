from django.contrib import admin
from .models import Cliente, Persona, Proveedor, Producto, Venta, Taller
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Persona)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Taller)