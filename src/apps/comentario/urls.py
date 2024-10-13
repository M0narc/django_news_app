from django.urls import path
from . import views

urlpatterns = [
    path('articulo/<int:articulo_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
]