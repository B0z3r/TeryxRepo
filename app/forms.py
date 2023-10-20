from django import forms
from .models import Persona, Cliente

class ColaboradorForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
