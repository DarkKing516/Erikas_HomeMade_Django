from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import RolForm

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'roles/listar_roles.html', {'roles': roles})

def crear_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_roles')
    else:
        form = RolForm()
    return render(request, 'roles/crear_rol.html', {'form': form})

def editar_rol(request, id_rol):
    rol = get_object_or_404(Rol, pk=id_rol)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_roles')
    else:
        form = RolForm(instance=rol)
    return render(request, 'roles/editar_rol.html', {'form': form})

def eliminar_rol(request, id_rol):
    rol = get_object_or_404(Rol, pk=id_rol)
    if request.method == 'POST':
        rol.delete()
        return redirect('usuarios:listar_roles')
    return render(request, 'roles/eliminar_rol.html', {'rol': rol})