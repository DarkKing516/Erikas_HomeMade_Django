from django.contrib import admin
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo_productos, name='catalogo'),
]
