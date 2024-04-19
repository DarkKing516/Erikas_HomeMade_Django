from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
# def index(request):
#     return HttpResponse("Pagina principal")

def index(request):
    return render(request, 'index.html')
