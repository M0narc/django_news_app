from django.urls import path
from . import views 
from apps.comentario.views import agregar_comentario, eliminar_comentario

urlpatterns = [
    path('', views.ArticuloSearchAndFilterView.as_view(), name='home'),
    path('articulo/<slug:slug>/comentario/', agregar_comentario, name='agregar_comentario'),  
    path('comentario/<slug:slug>/eliminar/', eliminar_comentario, name='eliminar_comentario'),  
    path('articulo/<slug:slug>', views.articulo_detalle, name='detalle_articulo'),  
]