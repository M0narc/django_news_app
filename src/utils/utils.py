from django.shortcuts import redirect


# from django.contrib.auth.decorators import login_required    ###para usar @login required

def redirect_authenticated_user(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('/')  # Redirigir a la página deseada
        return view(request)
    return wrapper
