from django.conf.urls import *
from django.urls import include, path
from django.http import HttpResponse
from . import views
app_name = 'home'

handler400 = 'home.views.page_not_found'
handler403 = 'home.views.page_not_found'
handler404 = 'home.views.page_not_found'
# handler500 = 'home.views.page_not_found'
urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.home, name='catalogo'),
    path('dashboard/', views.home, name='dashboard'),

]