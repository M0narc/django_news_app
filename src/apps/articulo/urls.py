from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('articulo/<int:id>/', views.articulo_detalle, name='articulo_detalle'),

]
