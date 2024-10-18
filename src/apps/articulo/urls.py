from django.urls import path
from .views import ArticuloDetalleView, ComentarioView, ArticuloUpdateView, ArticuloDeleteView,HomeView
from apps.comentario.views import agregar_comentario

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articulo/editar/<slug:slug>/', ArticuloUpdateView.as_view(), name='editar_articulo'),
    path('articulo/eliminar/<slug:slug>/', ArticuloDeleteView.as_view(), name='eliminar_articulo'),
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'), 
    path('articulo/<slug:slug>/comentar/', ComentarioView.as_view(), name='comentar_articulo'), 
    path('articulo/<slug:slug>', ArticuloDetalleView.as_view(), name='detalle_articulo'),  
    

]