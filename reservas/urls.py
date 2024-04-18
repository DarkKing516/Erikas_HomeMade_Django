from django.contrib import admin
from django.urls import path
from . import views as viewsReservas

urlpatterns = [
    path('hello/', viewsReservas.hello),
]
