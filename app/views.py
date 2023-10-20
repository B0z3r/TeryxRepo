from django.shortcuts import render
from .forms import ColaboradorForm, ClienteForm


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

   # clientes = ClienteForm.objects.all()

    return render(request, 'app/histCliente/agregar_cliente.html', data)