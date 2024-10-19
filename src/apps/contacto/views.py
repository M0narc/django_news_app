from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f'Mensaje de {name}',  
                message,  
                email,  
                [settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )
            return render(request, 'contacto/contacto_exitoso.html')  
    else:
        form = ContactForm()
    
    return render(request, 'contacto/contactanos.html', {'form': form})
