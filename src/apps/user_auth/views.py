from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomLoginForm
from utils.utils import redirect_authenticated_user
import logging


logger = logging.getLogger(__name__)

@redirect_authenticated_user
def register(request):
    if request.method == 'POST':
        logger.info('Intento de registro por un nuevo usuario.')
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info('Usuario registrado exitosamente: %s', user.username)
            return redirect('home')
        else:
            logger.warning('Error en el formulario de registro. Errores: %s', form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


@redirect_authenticated_user
def login_view(request):
    if request.method == 'POST':
        logger.info('Intento de inicio de sesión.')
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info('Inicio de sesión exitoso para el usuario: %s', username)
                return redirect('home')
            else:
                logger.warning('Fallo en la autenticación. Usuario: %s', username)
        else:
            logger.warning('Formularo de inicio de sesion invalido. errores: %s', form.errors)
    else:
        logger.info('Vista de inicio de sesión accesada por %s', request.user)

    form = CustomLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logger.info('Cierre de sesión para el usuario: %s', request.user.username)
    logout(request)
    return redirect('login')
