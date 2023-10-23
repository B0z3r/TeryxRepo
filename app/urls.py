from django.urls import path
from .views import  inicio_admin, regcolaborador, agregar_cliente, listar_cliente, modificar_cliente, eliminar_cliente, home
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('accounts/', auth_views.LoginView.as_view(), name='login'),
    path('inicio-admin/', inicio_admin, name="inicio_admin"),
    path('regcolaborador/', regcolaborador, name="regcolaborador"),
    path('agregar-cliente/', agregar_cliente, name="agregar_cliente"),
    path('listar-cliente/', listar_cliente, name="listar_cliente"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('home/', home, name="home"),
]
