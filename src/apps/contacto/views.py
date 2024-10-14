from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto/contactanos.html')