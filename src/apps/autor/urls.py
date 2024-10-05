from django.urls import path
from . import views

urlpatterns = [
    path('', views.autor_view, name='index'),
]