from django.urls import path
from .views import  inicio_admin,regcolaborador, agregar_cliente, listar_cliente, modificar_cliente, eliminar_cliente, inicio_vendedor, inicio_mecanico,\
agregar_producto,listar_producto, modificar_producto, eliminar_producto, agregar_proveedor, listar_proveedor, modificar_proveedor, eliminar_proveedor,\
agregar_taller, listar_taller, modificar_taller, eliminar_taller, agregar_venta, listar_venta, modificar_venta, eliminar_venta, agregar_historial, \
listar_historial, modificar_historial,  eliminar_historial
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path('accounts/', auth_views.LoginView.as_view(), name='login'),
    path('inicio-admin/', inicio_admin, name="inicio_admin"),
    path('inicio-vendedor/', inicio_vendedor, name="inicio_vendedor"),
    path('inicio-mecanico/', inicio_mecanico, name="inicio_mecanico"),
    path('regcolaborador/', regcolaborador, name="regcolaborador"),
    path('agregar-cliente/', agregar_cliente, name="agregar_cliente"),
    path('listar-cliente/', listar_cliente, name="listar_cliente"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('listar-proveedor/', listar_proveedor, name="listar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('agregar-taller/', agregar_taller, name="agregar_taller"),
    path('listar-taller/', listar_taller, name="listar_taller"),
    path('modificar-taller/<id>/', modificar_taller, name="modificar_taller"),
    path('eliminar-taller/<id>/', eliminar_taller, name="eliminar_taller"),
    path('agregar-venta/', agregar_venta, name="agregar_venta"),
    path('listar-venta/', listar_venta, name="listar_venta"),
    path('modificar-venta/<id>/', modificar_venta, name="modificar_venta"),
    path('eliminar-venta/<id>/', eliminar_venta, name="eliminar_venta"),
    path('agregar-historial/', agregar_historial, name="agregar_historial"),
    path('listar-historial/', listar_historial, name="listar_historial"),
    path('modificar-historial/<id>/', modificar_historial, name="modificar_historial"),
    path('eliminar-historial/<id>/', eliminar_historial, name="eliminar_historial"),
    path('crear-venta/', views.crear_venta, name='crear_venta'),
    path('listar-datos/', views.listar_datos, name='listar_datos'),
    

]
