from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm): 

    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "email", "password", "provincia", "localidad"]  
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'password': forms.PasswordInput(attrs={'class': 'form-control'}), 
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'apellido': forms.TextInput(attrs={'class': 'form-control'}), 
            'provincia': forms.Select(attrs={'class': 'form-select'}),
            'localidad': forms.Select(attrs={'class': 'form-select'}), 
        }
    
    def save(self, commit=True):
        usuario = super().save(commit=False)
        # Generar el username basado en el nombre y apellido
        username = (usuario.nombre[0] + usuario.apellido).lower()
        usuario.username = username
        
        if commit:
            usuario.save()
        return usuario
