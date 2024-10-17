from django.urls import path
from .views import ComentarioDeleteView, agregar_comentario

urlpatterns = [
    path('articulo/<int:articulo_id>/comentario/', agregar_comentario, name='agregar_comentario'),
    path('comentario/eliminar/<int:pk>/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
]