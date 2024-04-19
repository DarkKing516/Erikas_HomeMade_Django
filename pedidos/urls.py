from django.contrib import admin
from django.urls import path
from . import views as viewsPedidos
app_name = 'pedidos'

urlpatterns = [
    path('hello/', viewsPedidos.hello),
]
