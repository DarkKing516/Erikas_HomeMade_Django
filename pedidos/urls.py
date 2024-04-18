from django.contrib import admin
from django.urls import path
from . import views as viewsPedidos

urlpatterns = [
    path('hello/', viewsPedidos.hello),
]
