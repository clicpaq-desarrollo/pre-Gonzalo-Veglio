from django import forms
from .models import Provincia, Localidad

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
        }


class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-select'}),
        }
