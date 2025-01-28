# usuarios/forms.py
from django import forms
from .models import *


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(
        attrs={'class': 'inputField', 'id': 'email', 'placeholder': 'Email'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'inputField', 'id': 'password', 'placeholder': 'Contraseña'}))
