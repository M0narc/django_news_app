from django.contrib import admin
from .models import Articulo

class ArticuloCustom(admin.ModelAdmin):
    fields = ('fecha_publicada','titulo','autor')
    list_display = ('fecha_publicada','autor', 'titulo', )
    search_fields = ('titulo','autor__nombre', 'autor__apellido')
    list_per_page = 20
admin.site.register(Articulo, ArticuloCustom)