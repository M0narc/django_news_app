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

            # Enviar el correo
            send_mail(
                f'Mensaje de {name}',  # Asunto
                message,  # Cuerpo del mensaje
                email,  # Remitente
                [settings.EMAIL_HOST_USER],  # Destinatario
                fail_silently=False,
            )
            return render(request, 'contacto/contacto_exitoso.html')  # Crear plantilla de éxito
    else:
        form = ContactForm()
    
    return render(request, 'contacto/contactanos.html', {'form': form})
