from django.urls import path
from .views import ArticuloDetalleView, ComentarioView, home_view, Categoria_vista, Resultado_vista
from apps.comentario.views import agregar_comentario

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'),  
    path('articulo/<slug:slug>/', ArticuloDetalleView.as_view(), name='detalle_articulo'),
    path('articulo/<slug:slug>/comentar/', ComentarioView.as_view(), name='comentar_articulo'),
    path('categoria/<slug:slug>', Categoria_vista.as_view(), name= 'categoria'),
    path('buscar/', Resultado_vista.as_view(), name='buscar'),
]