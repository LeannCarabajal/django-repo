from django.db import models
from django.contrib.auth.models import User
class Nota(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nota')
