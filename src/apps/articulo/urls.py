from django.urls import path
from . import views
from apps.comentario.views import agregar_comentario, eliminar_comentario

urlpatterns = [
    path('', views.home_view, name='home'),
    
    # Comentarios
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'),
    path('comentario/<slug:slug>/eliminar/', eliminar_comentario, name='eliminar_comentario'),
    
    # Artículos
    path('articulo/<slug:slug>/editar/', views.editar_articulo, name='editar_articulo'), 
    path('articulo/<slug:slug>', views.articulo_detalle, name='detalle_articulo'),         
    path('articulo/<slug:slug>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),  
    
    # Categorías
    path('categoria/<slug:slug>', views.Categoria_vista.as_view(), name='categoria'),
    
    # Búsqueda
    path('buscar/', views.Resultado_vista.as_view(), name='buscar'),
]
