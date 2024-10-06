from django.contrib import admin
from .models import Articulo

class ArticuloCustom(admin.ModelAdmin):
    fields = ('fecha_publicada','titulo',)
    list_display = ('fecha_publicada',)
    search_fields = ('titulo',)

admin.site.register(Articulo, ArticuloCustom)