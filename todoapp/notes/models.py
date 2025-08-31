from django.db import models

# Create your models here.
class Notas(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    titulo = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(blank=True, null=True)
   