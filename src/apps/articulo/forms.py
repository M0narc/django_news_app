from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria', 'imagen_portada']  # Incluye imagen_portada
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del artículo'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe el contenido aquí...'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Añade un widget para el campo de imagen
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'categoria': 'Categoría',
            'imagen_portada': 'Imagen de Portada',
        }
