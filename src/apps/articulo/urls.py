from django.urls import path
from apps.articulo.views import home_view, articulos_por_categoria, articulo_detalle, buscar_articulos
from apps.comentario.views import agregar_comentario, eliminar_comentario

urlpatterns = [
    path('', home_view, name='home'),
    path('categoria/<int:categoria_id>/', articulos_por_categoria, name='articulos_por_categoria'),
    path('buscar/', buscar_articulos, name='buscar_articulos'),
    path('articulo/<int:articulo_id>/comentario/', agregar_comentario, name='agregar_comentario'),  
    path('comentario/<int:comentario_id>/eliminar/', eliminar_comentario, name='eliminar_comentario'),  
    path('articulo/<int:articulo_id>/', articulo_detalle, name='detalle_articulo'),  
]