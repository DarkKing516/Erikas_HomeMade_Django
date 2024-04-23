from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Permiso),
admin.site.register(Rol),
# admin.site.register(RolxPermiso),
admin.site.register(Usuario),