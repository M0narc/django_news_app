from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'fecha_publicada']  # Incluir los campos que desees editar
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe el contenido aquí...'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'categoria': 'Categoría',
            'fecha_publicada': 'Fecha de Publicación',
        }
