from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ClienteForm,CustomUserCreationForm, ProductoForm, ProveedorForm, TallerForm
from .models import Cliente, Producto, Proveedor, Taller
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
    return render(request, 'app/histCliente/modificar_cliente.html', data)

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_cliente")

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado Correctamente!")
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario

    return render(request, 'app/Productos/agregar_producto.html', data) 

def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'app/Productos/listar_producto.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    data = {
        'form': ProductoForm(instance = producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_producto")
        data["form"] = formulario
    return render(request, 'app/Productos/modificar_producto.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_producto")

def agregar_proveedor(request):
    data = {
        'form': ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Registrado Correctamente!")
            return redirect(to="listar_proveedor")
        else:
            data["form"] = formulario

    return render(request, 'app/proveedor/agregar_proveedor.html', data) 

def listar_proveedor(request):
    proveedor = Proveedor.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(proveedor, 5)
        proveedor = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': proveedor,
        'paginator': paginator
    }

    return render(request, 'app/proveedor/listar_proveedor.html', data)

def modificar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    data = {
        'form': ProveedorForm(instance = proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_proveedor")
        data["form"] = formulario
    return render(request, 'app/proveedor/modificar_proveedor.html', data)

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    proveedor.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_proveedor")

def agregar_taller(request):
    data = {
        'form': TallerForm()
    }
    if request.method == 'POST':
        formulario = TallerForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agendamiento Creado Correctamente!")
            return redirect(to="listar_taller")
        else:
            data["form"] = formulario

    return render(request, 'app/taller/agregar_taller.html', data) 

def listar_taller(request):
    taller = Taller.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(taller, 5)
        taller = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': taller,
        'paginator': paginator
    }

    return render(request, 'app/taller/listar_taller.html', data)

def modificar_taller(request, id):
    taller = get_object_or_404(Taller, pk=id)
    data = {
        'form': TallerForm(instance = taller)
    }
    if request.method == 'POST':
        formulario = TallerForm(data=request.POST, instance=taller)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_taller")
        data["form"] = formulario
    return render(request, 'app/taller/modificar_taller.html', data)

def eliminar_taller(request, id):
    taller = get_object_or_404(Taller, pk=id)
    taller.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_taller")