from django import forms
from .models import Persona, Cliente, Producto, Proveedor, Taller, Venta, Detalle_venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ColaboradorForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Nombre Usuario', max_length=20)
    rut = forms.IntegerField(label='Rut')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre Completo', max_length=100)
    fono = forms.IntegerField(label='Teléfono')
    email = forms.EmailField(label='Correo Electrónico', max_length=100)
    tipo_perfil = forms.ChoiceField(label='Tipo de Perfil', choices=[(0, 'Administrador'), (1, 'Vendedor'), (2, 'Mecánico')],widget=forms.Select)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    class Meta:
        model = User
        fields = ["username", "rut", "password1", "password2","first_name", "fono", "email","tipo_perfil"]


class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__' 


class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = '__all__' 

class TallerForm(forms.ModelForm):
    
    class Meta:
        model = Taller
        fields = '__all__' 

        widgets = {
            "fecha_ingreso": forms.SelectDateWidget(),
            "fecha_termino": forms.SelectDateWidget()
        }

class VentaForm(forms.ModelForm):
    
    class Meta:
        model = Venta
        fields = '__all__' 

        widgets = {
            "fecha": forms.SelectDateWidget(),
        }

class HistorialForm(forms.ModelForm):
    
    class Meta:
        model = Detalle_venta
        fields = ["id_detalle","tipo_servicio", "venta_id_venta", "producto_id_producto", "cliente_rut_cliente", "persona_rut_colaborador", "taller_id_taller"] 
