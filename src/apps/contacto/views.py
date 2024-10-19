from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm
import logging


logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')


def contacto(request):
    if request.method == 'POST':
        logger.info('Formulario de contacto enviado por %s', request.user)
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
            logger.info('Correo enviado exitosamente de %s a %s', email, settings.EMAIL_HOST_USER)
            return render(request, 'contacto/contacto_exitoso.html')  
    else:
        logger.info('Vista de contacto accesada por %s', request.user)
        form = ContactForm()
    
    return render(request, 'contacto/contactanos.html', {'form': form})
