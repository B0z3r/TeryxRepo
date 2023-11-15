from django import forms
from .models import Persona, Cliente, Producto, Proveedor, Taller, Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class ColaboradorForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    alphanumeric_regex = re.compile(r'^[a-zA-Z]+$')

    username = forms.CharField(
        label='Nombre Usuario',
        max_length=20,
        min_length=5,
        widget=forms.TextInput(attrs={'required': False})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'required': False})
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'required': False})
    )
    first_name = forms.CharField(
        label='Nombre Completo',
        max_length=100,
        widget=forms.TextInput(attrs={'required': False})
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=100,
        widget=forms.EmailInput(attrs={'required': False})
    )
    tipo_perfil = forms.ChoiceField(
        label='Tipo de Perfil',
        choices=[(0, 'Administrador'), (1, 'Vendedor'), (2, 'Mecánico')],
        widget=forms.Select(attrs={'required': False})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not self.alphanumeric_regex.match(username):
            raise ValidationError('El nombre de usuario debe contener solo letras mayúsculas y minúsculas.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "email", "tipo_perfil"]

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
        fields = ['fecha', 'descripcion', 'total', 'tipopago', 'tipo_servicio', 'producto_id_producto', 'taller_id_taller', 'cliente_rut_cliente'] 

        fecha = forms.DateField(
        widget=forms.SelectDateWidget(),
        input_formats=['%Y-%m-%d'],  # Formato de fecha deseado
    )

class tventa(forms.ModelForm):
    
    class Meta:
        model = Venta
        fields = ["total","tipopago"]
        widgets = {
            "fecha": forms.SelectDateWidget(),
        }

class tcliente(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ["rut_cliente","nombre_cliente","apePaterno","apeMaterno",]

class ttaller(forms.ModelForm):
    
    class Meta:
        model = Taller
        fields = ["id_taller","estado", "modelo_bicicleta","tipo_arreglo", "fecha_ingreso","fecha_termino",]   
        widgets = {
            "fecha_ingreso": forms.SelectDateWidget(),
            "fecha_termino": forms.SelectDateWidget()
 
        }
