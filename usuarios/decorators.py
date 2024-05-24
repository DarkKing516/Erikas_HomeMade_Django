from django.shortcuts import redirect

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            # Si el usuario no ha iniciado sesión, redirigir al formulario de inicio de sesión
            return redirect('usuarios:requestLogin')
        return view_func(request, *args, **kwargs)
    return wrapper
