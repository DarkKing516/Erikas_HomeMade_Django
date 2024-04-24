from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied
from .models import Rol

@receiver(pre_delete, sender=Rol)
def prevent_deletion_of_special_roles(sender, instance, **kwargs):
    # Verificar si el ID del rol es 0 o 1
    if instance.pk in [1, 2]:
        # Generar una excepción o un mensaje de error para evitar la eliminación del rol
        raise PermissionDenied("No se puede eliminar este rol.")
