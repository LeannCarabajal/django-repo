from rest_framework import serializers
from ..models import Evento, Baliza, Sala, Sesion

from django.utils import timezone


class EventoSerializer(serializers.ModelSerializer):

    baliza_mac = serializers.CharField(source="mac.mac", read_only=True)
    nombre_sala = serializers.CharField(source="sala.nombre", read_only=True)

    mac = serializers.CharField(write_only=True)
    sala = serializers.CharField(write_only=True)

    class Meta:
        model = Evento
        fields = ["id", "baliza_mac", "nombre_sala", "mac", "sala", "rssi", "action", "fecha",]

    def create(self, validated_data):

        mac_value = validated_data.pop("mac")
        sala_value = validated_data.pop("sala")

        try: 
            baliza = Baliza.objects.get(mac=mac_value)
        except Baliza.DoesNotExist:
            raise serializers.ValidationError(f"La baliza con MAC '{mac_value}' no está registrada.")
        
        try:
            sala = Sala.objects.get(nombre=sala_value)
        except Sala.DoesNotExist:
            raise serializers.ValidationError(f"La sala con nombre '{sala_value}' no está reg.")

        evento = Evento.objects.create(mac=baliza, sala=sala, **validated_data)

        if evento.action == "IN":
            sesion_abierta = Sesion.objects.filter(baliza=baliza, sala=sala, estado=True).first()
            print("Sesión abierta existente:", sesion_abierta)
            if not sesion_abierta:
                print("Creando sesión nueva...")
                Sesion.objects.create(
                    baliza=baliza,
                    sala=sala,
                    estado=True,
                    fecha_entrada=timezone.now(),
                )
        elif evento.action == "OUT":
            sesion_abierta = Sesion.objects.filter(
                baliza=baliza, sala=sala, estado=True
            ).first()
            if sesion_abierta:
                sesion_abierta.fecha_salida = timezone.now()
                sesion_abierta.estado = False
                sesion_abierta.save()
        return evento
    



