from django.shortcuts import redirect

def redirect_authenticated_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')  # si no tenemos ‘home' y tenemos '/’. poner eso
        return view_func(request, *args, **kwargs) 

       # si no esta autenticado te redirije a la pagina correspondiente
    return _wrapped_view


