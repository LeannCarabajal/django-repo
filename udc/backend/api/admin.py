from django.contrib import admin
from .models import Sala, Baliza, Evento, Sesion

# Register your models here.

admin.site.register(Sala)
admin.site.register(Baliza)
admin.site.register(Evento)
admin.site.register(Sesion)