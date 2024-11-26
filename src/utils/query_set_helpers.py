from django.utils import timezone
from django.db.models import Q
from apps.articulo.models import Articulo

class QuerySetBase:
    def obtener_queryset(self):
        return Articulo.objects.filter(fecha_publicada__lte=timezone.now())

class FiltroCategoria:
    def filtrar_por_categoria(self, queryset, categoria):
        if categoria:
            return queryset.filter(categoria__nombre=categoria)
        return queryset

class BusquedaTitulo:
    def buscar_por_query(self, queryset, query):
        if query:
            return queryset.filter(
                Q(titulo__icontains=query) | Q(categoria__nombre__icontains=query)
            ).distinct()
        return queryset

class OrdenarArticulos:
    def ordenar(self, queryset, orden):
        return queryset.order_by(orden if orden else '-fecha_publicada')
