from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Libro)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Autor)
admin.site.register(RedesAutor)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Imagenes)