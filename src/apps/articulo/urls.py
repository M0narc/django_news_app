from django.urls import path
from . import views 
from apps.comentario.views import agregar_comentario, eliminar_comentario

urlpatterns = [
    path('', views.home_view, name='home'),
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'),  
    path('comentario/<int:comentario_id>/eliminar/', eliminar_comentario, name='eliminar_comentario'),  
    path('articulo/<slug:slug>/', views.articulo_detalle, name='detalle_articulo'),  
    path('categoria/<slug:slug>', views.Categoria_vista.as_view(), name= 'categoria'),
    path('buscar/', views.Resultado_vista.as_view(), name='buscar'),
]