from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .forms import  tventa,ttaller,tcliente,ClienteForm,CustomUserCreationForm, ProductoForm, ProveedorForm, TallerForm, VentaForm
from .models import Cliente, Producto, Proveedor, Taller, Venta
from django.contrib  import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def login(request):
    return render(request, 'registration/accounst/login.html')

def micuenta(request):
    return render(request, 'app/Micuenta/micuenta.html')

def gestionar_productos(request):
    return render(request, 'app/productos/gestionar_productos.html')


def inicio_admin(request):
    clientes = Cliente.objects.all()
    total_clientes = clientes.count()
    proveedores = Proveedor.objects.all()
    total_proveedores = proveedores.count()
    data = {
        'clientes': clientes,
        'total_clientes': total_clientes,
        'proveedores': proveedores,
        'total_proveedores': total_proveedores
    }
    return render(request, 'app/inicio_admin.html', data)

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

@permission_required('app.view_colaborador')
def listar_colaborador(request):
    persona = User.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(persona, 5)
        personas = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': personas,
        'paginator': paginator
    }

    return render(request, 'app/colaborador/listar_colaborador.html', data)

def listar_micuenta(request):
    persona = User.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(persona, 5)
        personas = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': personas,
        'paginator': paginator
    }

    return render(request, 'app/Micuenta/micuenta.html', data)
    
@permission_required('app.change_colaborador')
def modificar_colaborador(request, id):
    persona = get_object_or_404(User, pk=id)
    data = {
        'form': CustomUserCreationForm(instance = persona)
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_colaborador")
           
        data["form"] = formulario
    return render(request, 'app/colaborador/modificar_colaborador.html', data)


@permission_required('app.change_colaborador')
def modificar_cuenta(request, id):
    persona = get_object_or_404(User, pk=id)
    data = {
        'form': CustomUserCreationForm(instance = persona)
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=persona)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="micuenta")
           
        data["form"] = formulario
        return render(request, 'app/Micuenta/micuenta.html', data)

@permission_required('app.delete_colaborador')
def eliminar_colaborador(request, id):
    persona = get_object_or_404(User, pk=id)
    persona.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_colaborador")

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

def historial_cliente(request, id):
    cliente = get_object_or_404(Cliente, rut_cliente=id)
    
    ventas = cliente.venta_set.all()
    return render(request, 'app/Cliente/historial_cliente.html', {'cliente': cliente, 'ventas': ventas})

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
            return redirect(to="list_taller")
        else:
            data["form"] = formulario

    return render(request, 'app/taller/agregar_taller.html', data) 

@permission_required('app.delete_taller')
def eliminar_taller(request, id):
    taller = get_object_or_404(Taller, pk=id)
    taller.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="list_taller")

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

def crear_venta(request):
    if request.method == 'POST':
        taller_form = ttaller(request.POST)

        if taller_form.is_valid():
            taller_form.save()

            return redirect('crear_venta') 

    else:
        taller_form = ttaller()

    return render(request, 'app/taller/crear_venta.html', {'taller_form': taller_form})

def list_taller(request):
    ventas = Venta.objects.all()
    talleres = Taller.objects.all()
    clientes = Cliente.objects.all()

    datos_combinados = []

    for venta, taller, cliente in zip(ventas, talleres, clientes):
        datos_combinados.append({
            'id_taller': taller.id_taller,
            'total': venta.total,
            'tipopago': venta.tipopago,
            'fecha_ingreso': taller.fecha_ingreso,
            'fecha_termino': taller.fecha_termino,
            'tipo_arreglo': taller.tipo_arreglo,
            'estado': taller.get_estado_display(),
            'modelo_bicicleta': taller.modelo_bicicleta,
            'nombre_cliente': cliente.nombre_cliente,
            'apePaterno': cliente.apePaterno,
            'apeMaterno': cliente.apeMaterno,
            'id_venta': venta.id_venta,
            'rut_cliente': cliente.rut_cliente,
        })

    page = request.GET.get('page', 1)

    paginator = Paginator(datos_combinados, 5)
    try:
        datos_combinados = paginator.page(page)
    except PageNotAnInteger:
        datos_combinados = paginator.page(1)
    except EmptyPage:
        datos_combinados = paginator.page(paginator.num_pages)

    return render(request, 'app/taller/list_taller.html', {'datos_combinados': datos_combinados})

@permission_required('app.change_taller')
def modificar_taller(request, id):
    taller = get_object_or_404(Taller, pk=id)
    cliente = get_object_or_404(Cliente, pk=id)
    venta = get_object_or_404(Venta, pk=id)


    if request.method == 'POST':
        taller_form = ttaller(request.POST, instance=taller)
        cliente_form = tcliente(request.POST, instance=cliente)
        venta_form = tventa(request.POST, instance=venta)

        if venta_form.is_valid() and cliente_form.is_valid() and taller_form.is_valid():
            cliente = cliente_form.save()
            taller = taller_form.save()
            venta = venta_form.save()
            taller.cliente = cliente
            taller.venta = venta
            taller.save()
            return redirect('list_taller') 

    else:
        venta_form = tventa()
        cliente_form = tcliente()
        taller_form = ttaller()

        return render(request, 'app/taller/modificar_taller.html',{
        'venta_form': venta_form,
        'cliente_form': cliente_form,
        'taller_form': taller_form,
    })

def test_view(request):
    return render(request, 'app/test.html')


def cambio_pass(request):
    return render(request, 'app/Micuenta/cambio_pass.html')

def cambio_pass(request):
    return render(request, 'app/Micuenta/cambio_pass.html')





#cambio contraseña
class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'app/Micuenta/cambio_pass.html'
    success_url = reverse_lazy('micuenta')

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['password_change'] = self.request.session.get('password_changed', False) 
        return context

    def form_valid (self, form):
        messages.success(self.request, 'Cambio contraseña exitoso')
        update_session_auth_hash(self.request, form.user)
        self.request.session['password_changed'] = True
        return super().form_valid(form)
  

  
    def form_invalid(self, form):
        messages.error(self.request, 'Cambio contraseña inválida')
        return super().form_invalid(form)
    


from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Producto
from .forms import ProductoForm
from django.http import Http404




@permission_required(['app.add_producto', 'app.view_producto', 'app.change_producto', 'app.delete_producto'])
def gestionar_productos(request, id=None):
    # Obtener todos los productos
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': productos, 'paginator': paginator}

    # Agregar producto
    if request.user.has_perm('app.add_producto'):
        data['form'] = ProductoForm()

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto Registrado Correctamente!")
                return redirect(to="gestionar_productos")
            else:
                data["form"] = formulario

    # Modificar producto
    if id and request.user.has_perm('app.change_producto'):
        producto = get_object_or_404(Producto, pk=id)
        data['form'] = ProductoForm(instance=producto)

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto Modificado Correctamente!")
                return redirect(to="gestionar_productos")
            else:
                data["form"] = formulario

    # Eliminar producto
    if id and request.user.has_perm('app.delete_producto'):
        producto = get_object_or_404(Producto, pk=id)
        producto.delete()
        messages.success(request, "Producto Eliminado Correctamente!")
        return redirect(to="gestionar_productos")

    return render(request, 'app/Productos/gestionar_productos.html', data)




