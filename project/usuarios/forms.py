from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm): 
    
    class Meta:
        model = Usuario
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'}), 
            'fecha_creacion': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'apellido': forms.TextInput(attrs={'class': 'form-control'}), 
            'provincia': forms.Select(attrs={'class': 'form-select'}),
            'localidad': forms.Select(attrs={'class': 'form-select'}), 
        }
        