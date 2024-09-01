from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm): 
 
      class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {
            'razon_social': forms.Select(attrs={'class': 'form-select mt-2'}),
            'nombre_destinatario': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'apellido_destinatario': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'telefono_destinatario': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'email_destinatario': forms.EmailInput(attrs={'class': 'form-control mt-2'}), 
            'direccion_entrega': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'ciudad_entrega': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'provincia_entrega': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'codigo_postal_entrega': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'estado': forms.TextInput(attrs={'class': 'form-control mt-2'}), 
            'creado_por': forms.Select(attrs={'class': 'form-select mt-2'}), 
         }