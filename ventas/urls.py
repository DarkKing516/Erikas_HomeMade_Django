from django.contrib import admin
from django.urls import path
from . import views as viewsVentas
app_name = 'ventas'

urlpatterns = [
    path('hello/', viewsVentas.hello),
]
