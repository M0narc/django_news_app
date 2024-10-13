from django.shortcuts import redirect



def redirect_authenticated_user(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('/') 
        return view(request)
    return wrapper
