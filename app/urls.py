from django.urls import path
from .views import  gestionar_productos,cambio_pass,inicio_admin,regcolaborador, listar_colaborador, modificar_colaborador, eliminar_colaborador, agregar_cliente, listar_cliente,\
modificar_cliente, eliminar_cliente,generar_pdf,ProfilePasswordChangeView,\
historial_cliente,agregar_producto,listar_producto, modificar_producto, eliminar_producto, agregar_proveedor, listar_proveedor, modificar_proveedor, eliminar_proveedor,\
agregar_taller, modificar_taller, eliminar_taller, agregar_venta, listar_venta, modificar_venta, eliminar_venta,\
list_taller, agregar_cantidad_stock
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('accounts/', auth_views.LoginView.as_view(), name='login'),
    path('inicio-admin/', inicio_admin, name="inicio_admin"),
    path('regcolaborador/', regcolaborador, name="regcolaborador"),
    path('listar-colaborador/', listar_colaborador, name="listar_colaborador"),
    path('modificar-colaborador/<int:id>/', modificar_colaborador, name="modificar_colaborador"),
    path('eliminar-colaborador/<id>/', eliminar_colaborador, name="eliminar_colaborador"),
    path('agregar-cliente/', agregar_cliente, name="agregar_cliente"),
    path('listar-cliente/', listar_cliente, name="listar_cliente"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('historial-cliente/<id>/', historial_cliente, name='historial_cliente'),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('listar-proveedor/', listar_proveedor, name="listar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('agregar-taller/', agregar_taller, name="agregar_taller"),
    path('listar-taller/', list_taller, name="list_taller"),
    path('modificar-taller/<id>/', modificar_taller, name="modificar_taller"),
    path('eliminar-taller/<id>/', eliminar_taller, name="eliminar_taller"),
    path('agregar-venta/', agregar_venta, name="agregar_venta"),
    path('listar-venta/', listar_venta, name="listar_venta"),
    path('modificar-venta/<id>/', modificar_venta, name="modificar_venta"),
    path('eliminar-venta/<id>/', eliminar_venta, name="eliminar_venta"),
    path('crear-venta/', views.crear_venta, name='crear_venta'),
    path('list-taller/', views.list_taller, name='list_taller'),
    path('test/', views.test_view, name='test_view'),
    path('micuenta/', views.micuenta, name='micuenta'),
    path('listar-micuenta/', views.listar_micuenta, name='listar_micuenta'),
    path('modificar_cuenta/', views.modificar_cuenta, name='modificar_cuenta'),
    path('cambio-pass/', views.cambio_pass, name='cambio_pass'),
    path('gestionar-productos/', gestionar_productos, name='gestionar_productos'),
    path('agregar_venta_y_listar_producto/', views.agregar_venta_and_listar_producto, name='agregar_venta_y_listar_producto'),
    path('password_change/',login_required (ProfilePasswordChangeView.as_view()),name='Profile_password_change',),
    path('generar-pdf/', generar_pdf, name='generar_pdf'),
    path('agregar-cantidad-stock/<int:producto_id>/', views.agregar_cantidad_stock, name='agregar_cantidad_stock'),
]
