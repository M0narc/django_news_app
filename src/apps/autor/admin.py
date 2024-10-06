from django.contrib import admin
from.models import Autor

# Register your models here.

class AutorCustom(admin.ModelAdmin):
    fields = ('id', 'nombre', 'apellido')
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre', 'email')

admin.site.register(Autor, AutorCustom)