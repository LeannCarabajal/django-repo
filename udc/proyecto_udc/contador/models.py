from django.db import models

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Baliza(models.Model):
    uuid = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion or self.uuid
    
class Evento(models.Model):
    ESTADOS = [
        ("IN", "Dentro del rango"),
        ("OUT", "Fuera del rango"),
    ]

    baliza = models.ForeignKey(Baliza, on_delete=models.CASCADE, related_name="eventos")
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="eventos")
    estado = models.CharField(max_length=3, choices=ESTADOS)
    fecha = models.DateTimeField()
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.baliza.uuid} - {self.sala.nombre} - {self.estado} - {self.fecha}"


class Sesion(models.Model):
    baliza = models.ForeignKey(Baliza, on_delete=models.CASCADE, related_name="sesiones")
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name="sesiones")
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.baliza.uuid} - {self.sala.nombre} ({self.fecha_entrada} → {self.fecha_salida or 'En curso'})"
