from django.shortcuts import render
from django.http import HttpResponse
from .models import Rol

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'listar_roles.html', {'roles': roles})