from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria']  
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Contenido del artículo'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
