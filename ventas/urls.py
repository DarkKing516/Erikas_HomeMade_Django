from django.contrib import admin
from django.urls import path
from . import views as viewsVentas

urlpatterns = [
    path('hello/', viewsVentas.hello),
]
