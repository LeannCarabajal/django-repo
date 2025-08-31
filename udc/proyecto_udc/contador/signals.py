from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Evento, Sesion

@receiver(post_save, sender=Evento)
def actualizar_sesion(sender, instance, created, **kwargs):
    if not created:
        return  # Solo nos interesa cuando se crea un evento

    baliza = instance.baliza
    sala = instance.sala

    if instance.estado == "IN":
        # Crear nueva sesión si no hay sesión abierta para esta baliza en esta sala
        Sesion.objects.get_or_create(
            baliza=baliza,
            sala=sala,
            fecha_salida__isnull=True,
            defaults={'fecha_entrada': instance.fecha}
        )
    elif instance.estado == "OUT":
        # Actualizar sesión abierta (fecha_salida) para esta baliza en esta sala
        try:
            sesion_abierta = Sesion.objects.get(
                baliza=baliza,
                sala=sala,
                fecha_salida__isnull=True
            )
            sesion_abierta.fecha_salida = instance.fecha
            sesion_abierta.save()
        except Sesion.DoesNotExist:
            # Por si llega un OUT sin un IN previo
            pass
