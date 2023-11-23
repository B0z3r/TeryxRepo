from django import forms
from .models import Persona, Cliente, Producto, Proveedor, Taller, Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from django.utils.safestring import mark_safe

class ColaboradorForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(forms.ModelForm):
      rut_cliente = forms.CharField(
        label='Rut Cliente',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el RUT del cliente'}),
        required=False,
    )

      nombre_cliente = forms.CharField(
        label='Nombre cliente',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa nombre del cliente'}),
        required=False,
    )

      apePaterno = forms.CharField(
        label='Apellido Paterno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el Apellido Paterno'}),
        required=False,
    )

      apeMaterno = forms.CharField(
        label='Apellido Materno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el Apellido Materno'}),
        required=False,
    )

      email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresa el Correo Electrónico'}),
        required=False,
    )

      fono = forms.IntegerField(
        label='Teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el Teléfono'}),
        required=False,
    )

      class Meta:
        model = Cliente
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    alphanumeric_regex = re.compile(r'^[a-zA-Z]+$')

    username = forms.CharField(
        label='Nombre Usuario',
        max_length=20,
        min_length=5,
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario'}),
        required=False, 
       
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña', 'required': False}),
        min_length=8,
        max_length=20,
        required=False,
      
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña', 'required': False}),
        min_length=8,
        max_length=20,
        required=False,
     
    )
    first_name = forms.CharField(
        label='Nombre Completo',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre completo', 'required': False}),
        required=False,
    )
    email = forms.EmailField(
        label='Correo Electrónico',
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico', 'required': False}),
        required=False,
    )
    tipo_perfil = forms.ChoiceField(
        label='Tipo de Perfil',
        choices=[(0, 'Administrador'), (1, 'Vendedor'), (2, 'Mecánico')],
        widget=forms.Select(attrs={'required': False}),
        required=False,
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
    
    class CustomWidget(forms.TextInput):
     def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs)
        button_html = '<button type="button">Mi Botón</button>'
        return mark_safe(f'{input_html} {button_html}')
     
    opc_consl_cat = [
        ('', 'Selecciona una opción....'),
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]
  
    nombre_producto = forms.CharField(
        label='Nombre Producto',
        widget=CustomWidget(attrs={'placeholder': 'Ingresa el nombre del producto', 'required': False}),
        required=False,
    )
    marca = forms.CharField(
        label='Marca',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa la marca del producto', 'required': False}),
        required=False,
    )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'placeholder': 'Ingresa la descripción del producto', 'cols': 30, 'rows': 3, 'required': False}),
        required=False,
    )
    precio_unitario = forms.DecimalField(
        label='Precio Unitario',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa el precio unitario', 'required': False}),
        required=False,
    )
    stock = forms.IntegerField(
        label='Stock',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa el stock del producto', 'required': False, 'class': 'no-spinner'}),
        required=False,
    )
    categoria = forms.ChoiceField(
        label='Categoría',
        choices=opc_consl_cat,
        widget=forms.Select(attrs={'placeholder': 'Selecciona una opción', 'required': False}),
        required=False,
    )

    nombre_proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),  # Asegúrate de ajustar el queryset según tus cambios en el modelo
        required=False,
    )

    fecha_registro = forms.DateField(
        label='Fecha Registro',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )
    
    class Meta:
        model = Producto
        fields = ["nombre_producto","marca","descripcion","precio_unitario","stock","categoria","nombre_proveedor","fecha_registro"]

class ProveedorForm(forms.ModelForm):
     
     opc_consl_cat = [
         ('', 'Selecciona una opción....'),
        [0,"Indumentaria"],
        [1,"Accesorio"],
        [2,"Repuestos"]
    ]
     
     nombre_proveedor = forms.CharField(
        label='Nombre Proveedor',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el nombre del proveedor', 'required': False}),
        required=False,
    )

     rut_proveedor = forms.IntegerField(
        label='RUT Proveedor',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa el RUT del proveedor', 'required': False}),
        required=False,
    )

     email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresa el correo electrónico del proveedor', 'required': False}),
        required=False,
    )

     fono = forms.IntegerField(
        label='Teléfono',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa el teléfono del proveedor', 'required': False}),
        required=False,
    )

     categoria = forms.ChoiceField(
        label='Categoría',
        choices=opc_consl_cat,
        widget=forms.Select(attrs={'placeholder': 'Selecciona una opción', 'required': False}),
        required=False,
    )

     pagina_web = forms.URLField(
        label='Página Web',
        widget=forms.URLInput(attrs={'placeholder': 'Ingresa la página web del proveedor', 'required': False}),
        required=False,
    )

     class Meta:
        model = Proveedor
        fields = '__all__' 

class TallerForm(forms.ModelForm):

    opc_tipo_arreglo = [
    [0,"Ajustes básicos"],
    [1,"Cambio de neumáticos"],
    [2,"Cambio Frenos"],
    [3,"Reparación de Cadena, Pedales y Bielas"],
    [4,"Ajuste de Suspensión"],
    ]

    opc_estado = [
        [0,"En proceso"],
        [1,"Términado"],
        [2,"Atrasado"],
    ]

    opc_estado_pago = [
    [0, "Pendiente"],
    [1, "Pagado"],
    ]

    fecha_ingreso = forms.DateField(
        label='Fecha Ingreso',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    fecha_termino = forms.DateField(
        label='Fecha Término',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
    )

    tipo_arreglo = forms.ChoiceField(
        label='Tipo de Arreglo',
        choices=opc_tipo_arreglo,
        widget=forms.Select(attrs={'placeholder': 'Selecciona una opción', 'required': False, 'id': 'id_tipo_arreglo'}),
        required=False,
    )

    valor = forms.IntegerField(
        label='Valor del Arreglo',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresa el Valor del Arreglo', 'required': False, 'id': 'id_valor'}),
        required=False,
    )

    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={'placeholder': 'Ingresa la Descipción del Arreglo', 'cols': 30, 'rows': 3, 'required': False, 'id': 'id_descripcion'}),
        required=False,
    )

    estado = forms.ChoiceField(
        label='Estado del Arreglo',
        choices = opc_estado,
        widget=forms.Select(attrs={'placeholder': 'Selecciona una Opción....', 'required': False}),
        required=False,
    )

    modelo_bicicleta = forms.CharField(
        label='Modelo de la Bicicleta',
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa el Modelo de la Bicicleta', 'required': False}),
        required=False,
    )

    estado_pago = forms.ChoiceField(
        label='Estado de Pago',
        choices=opc_estado_pago,
        widget=forms.Select(attrs={'placeholder': 'Ingresa el Estado de pago', 'required': False}),
        required=False,
    )

    abono = forms.IntegerField(
        label='Abono',
        widget=forms.NumberInput(attrs={'placeholder': 'Ingresar el Abono', 'required': False}),
        required=False,
    )
    
    class Meta:
        model = Taller
        fields = '__all__' 

class VentaForm(forms.ModelForm):
    
    class Meta:
        model = Venta
        fields = ['fecha', 'descripcion', 'total', 'tipopago', 'tipo_servicio', 'producto_id_producto', 'taller_id_taller'] 

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
