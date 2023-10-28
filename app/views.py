from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ClienteForm,CustomUserCreationForm, ProductoForm, ProveedorForm, TallerForm, VentaForm, HistorialForm
from .models import Cliente, Producto, Proveedor, Taller, Venta, Detalle_venta, Persona
from django.contrib  import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def login(request):
    return render(request, 'registration/accounst/login.html')

def inicio_admin(request):
    return render(request, 'app/inicio_admin.html')

def inicio_vendedor(request):
    return render(request, 'app/inicio_vendedor.html')

def inicio_mecanico(request):
    return render(request, 'app/inicio_mecanico.html')

@permission_required('app.add_regcolaborador')
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
        
    return render(request, 'app/colaborador/regcolaborador.html', data)

@permission_required('app.add_cliente')
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

    return render(request, 'app/Cliente/agregar_cliente.html', data)

@permission_required('app.view_cliente')
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

    return render(request, 'app/Cliente/listar_cliente.html', data)

@permission_required('app.change_cliente')
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
    return render(request, 'app/Cliente/modificar_cliente.html', data)

@permission_required('app.delete_cliente')
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_cliente")

@permission_required('app.add_producto')
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

@permission_required('app.view_producto')
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

@permission_required('app.change_producto')
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

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_producto")

@permission_required('app.add_proveedor')
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

@permission_required('app.view_proveedor')
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

@permission_required('app.change_proveedor')
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

@permission_required('app.delete_proveedor')
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    proveedor.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_proveedor")

@permission_required('app.add_taller')
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

@permission_required('app.view_taller')
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

@permission_required('app.change_taller')
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

@permission_required('app.delete_taller')
def eliminar_taller(request, id):
    taller = get_object_or_404(Taller, pk=id)
    taller.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_taller")

@permission_required('app.add_venta')
def agregar_venta(request):
    data = {
        'form': VentaForm()
    }
    if request.method == 'POST':
        formulario = VentaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Venta Creada Correctamente!")
            return redirect(to="listar_venta")
        else:
            data["form"] = formulario

    return render(request, 'app/venta/agregar_venta.html', data) 

@permission_required('app.view_venta')
def listar_venta(request):
    venta = Venta.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(venta, 5)
        venta = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': venta,
        'paginator': paginator
    }

    return render(request, 'app/venta/listar_venta.html', data)

@permission_required('app.change_venta')
def modificar_venta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    data = {
        'form': VentaForm(instance = venta)
    }
    if request.method == 'POST':
        formulario = VentaForm(data=request.POST, instance=venta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificada Correctamente!")
            return redirect(to="listar_venta")
        data["form"] = formulario
    return render(request, 'app/venta/modificar_venta.html', data)

@permission_required('app.delete_venta')
def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, pk=id)
    venta.delete()
    messages.success(request, "Eliminada Correctamente!")
    return redirect(to="listar_venta")

@permission_required('app.add_historial')
def agregar_historial(request):
    data = {
        'form': HistorialForm()
    }
    if request.method == 'POST':
        formulario = HistorialForm(data=request.POST)
        if formulario.is_valid():
            
            venta_id = formulario.cleaned_data['venta_id_venta']
            producto_id = formulario.cleaned_data['producto_id_producto']
            cliente_rut = formulario.cleaned_data['cliente_rut_cliente']
            colaborador_rut = formulario.cleaned_data['persona_rut_colaborador']
            taller_id = formulario.cleaned_data['taller_id_taller']

            venta = Venta.objects.get(id_venta=venta_id)
            producto = Producto.objects.get(id_producto=producto_id)
            cliente = Cliente.objects.get(rut_cliente=cliente_rut)
            colaborador = Persona.objects.get(rut_colaborador=colaborador_rut)
            taller = Taller.objects.get(id_taller=taller_id)

            detalle_venta = Detalle_venta(
                venta_id_venta=venta,
                producto_id_producto=producto,
                cliente_rut_cliente=cliente,
                persona_rut_colaborador=colaborador,
                taller_id_taller=taller
            )
        
            formulario.save()
            messages.success(request, "Historial Creado Correctamente!")
            return redirect(to="listar_historial")
        else:
            data["form"] = formulario

    return render(request, 'app/Historial/agregar_historial.html', data) 

@permission_required('app.view_historial')
def listar_historial(request):
    historial = Detalle_venta.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(historial, 5)
        historial = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': historial,
        'paginator': paginator
    }

    return render(request, 'app/Historial/listar_historial.html', data)

@permission_required('app.change_historial')
def modificar_historial(request, id):
    historial = get_object_or_404(Detalle_venta, pk=id)
    data = {
        'form': HistorialForm(instance = historial)
    }
    if request.method == 'POST':
        formulario = HistorialForm(data=request.POST, instance=historial)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_historial")
        data["form"] = formulario
    return render(request, 'app/Historial/modificar_historial.html', data)

@permission_required('app.delete_historial')
def eliminar_historial(request, id):
    historial = get_object_or_404(Detalle_venta, pk=id)
    historial.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_historial")
#probando esto
def lista_productos_por_cliente(request):
    clientes = Cliente.objects.all()
    data = []

    for cliente in clientes:
        productos_comprados = Detalle_venta.objects.filter(cliente_rut_cliente=cliente)
        data.append({'cliente': cliente, 'productos_comprados': productos_comprados})

    return render(request, 'tu_app/lista_productos.html', {'data': data})