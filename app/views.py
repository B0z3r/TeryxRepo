from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ClienteForm,CustomUserCreationForm
from .models import Cliente
from django.contrib  import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    return render(request, 'registration/accounst/login.html')

def inicio_admin(request):
    return render(request, 'app/inicio_admin.html')


def inicio_vendedor(request):
    return render(request, 'app/inicio_vendedor.html')


def inicio_mecanico(request):
    return render(request, 'app/inicio_mecanico.html')

def regcolaborador(request):
    
    data = {
        #ColaboradorForm()
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Colaborador Registrado Correctamente!")
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
            messages.success(request, "Cliente Registrado Correctamente!")
            return redirect(to="listar_cliente")
        else:
            data["form"] = formulario

    return render(request, 'app/histCliente/agregar_cliente.html', data)

def listar_cliente(request):
    clientes = Cliente.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(clientes, 5)
        clientes = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': clientes,
        'paginator': paginator
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
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_cliente")
        data["form"] = formulario
            #data["mensaje"] = "Cliente Modificado Exitosamente!"
        #else:
          

    return render(request, 'app/histCliente/modificar_cliente.html', data)

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_cliente")

