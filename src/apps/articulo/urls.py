from django.urls import path
from .views import ArticuloDetalleView, ComentarioView, HomeView, Categoria_vista, Resultado_vista, ArticuloUpdateView, ArticuloDeleteView
from apps.comentario.views import agregar_comentario

urlpatterns = [
    path('', views.ArticuloSearchAndFilter.as_view(), name='home'),
    path('articulo/editar/<slug:slug>/', ArticuloUpdateView.as_view(), name='editar_articulo'),
    path('articulo/eliminar/<slug:slug>/', ArticuloDeleteView.as_view(), name='eliminar_articulo'),
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'), 
    path('articulo/<slug:slug>/comentar/', ComentarioView.as_view(), name='comentar_articulo'), 
    path('comentario/<slug:slug>/eliminar/', eliminar_comentario, name='eliminar_comentario'),  
    path('articulo/<slug:slug>', views.articulo_detalle, name='detalle_articulo'),  
    

]