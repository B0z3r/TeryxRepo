from django.urls import path
from .views import  inicio_admin,regcolaborador, agregar_cliente, listar_cliente, modificar_cliente, eliminar_cliente, inicio_vendedor, inicio_mecanico
from django.contrib.auth import views as auth_views

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
    

   
]
