from django.contrib import admin
from django.urls import path
from . import views as viewsUsuarios

urlpatterns = [
    path('hello/', viewsUsuarios.hello),
    path('listar_roles/', viewsUsuarios.listar_roles, name='listar_roles'),

]
