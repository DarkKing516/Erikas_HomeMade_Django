from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reserva
from .forms import ReservaForm


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas:listar_reserva')  # Cambia 'pagina_de_exito' por la URL de la página a la que quieres redirigir después de crear la reserva
    else:
        form = ReservaForm()
    return render(request, 'crear_reserva.html', {'form': form})