from django.shortcuts import render, redirect, get_object_or_404
from .forms import ColaboradorForm, ClienteForm
from .models import Cliente


# Create your views here.


def login(request):
    return render(request, 'registration/accounst/login.html')


def inicio_admin(request):
    return render(request, 'app/inicio_admin.html')

def regcolaborador(request):
    
    data = {
        'form': ColaboradorForm()
    }
    if request.method == 'POST':
        formulario = ColaboradorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Colaborador Registrado Exitosamente!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/regcolaborador.html', data)


def agregar_cliente(request):

    data = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cliente Registrado Exitosamente!"
        else:
            data["form"] = formulario

    return render(request, 'app/histCliente/agregar_cliente.html', data)

def listar_cliente(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }

    return render(request, 'app/histCliente/listar_cliente.html', data)



def modificar_cliente(request, id):

    cliente = get_object_or_404(Cliente, pk=id)

    data = {
        'form': ClienteForm(instance = cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_cliente")
        data["form"] = formulario
            #data["mensaje"] = "Cliente Modificado Exitosamente!"
        #else:
          

    return render(request, 'app/histCliente/modificar_cliente.html', data)



def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect(to="listar_cliente")



def home(request):
    return render(request, 'app/home.html')
