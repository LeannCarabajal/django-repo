from django.db import models
from django.utils import timezone
# Create your models here.

class Baliza(models.Model):
    mac = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion or self.mac
    

class Sala(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class Evento(models.Model):
    ESTADOS = [
        ("IN", "Dentro del rango"),
        ("OUT", "Fuera del rango"),
    ]

    mac = models.ForeignKey(Baliza, on_delete=models.CASCADE, related_name="eventos")
    rssi = models.IntegerField()
    action = models.CharField(max_length=3, choices=ESTADOS)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="eventos")
    fecha = models.DateTimeField(default=timezone.now)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.mac.mac} - {self.sala.nombre} - {self.action} - {self.fecha}"


class Sesion(models.Model):
    baliza = models.ForeignKey(Baliza, on_delete=models.CASCADE, related_name="sesiones")
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="sesiones")
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    state = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.baliza.mac} - {self.sala.nombre} ({self.fecha_entrada} → {self.fecha_salida or 'En curso'})"
