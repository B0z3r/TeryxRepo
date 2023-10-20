from django.urls import path
from .views import home, inicio_admin, regcolaborador, agregar_cliente

urlpatterns = [
    path('', home, name="home"),
    path('inicio-admin/', inicio_admin, name="inicio_admin"),
    path('regcolaborador/', regcolaborador, name="regcolaborador"),
    path('agregar-cliente/', agregar_cliente, name="agregar_cliente"),
]
