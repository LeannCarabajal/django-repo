from django.db import models

class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    nombres = models.CharField(max_length=255, null = False, blank = False)
    apellido = models.CharField(max_length=255, null = False, blank = False)
    descripcion = models.TextField(blank = True, null = True)
    email = models.EmailField(unique = True, blank = True, null = True)
    web = models.URLField(blank=True,null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"
    

class RedesAutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="redes_sociales")
    plataforma = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField(null=False, unique=True, blank=False)

    def __str__(self):
        return f"{self.plataforma}: {self.url}"

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255, unique=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Subcategoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="subcategorias")
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    nombre = models.CharField(max_length=255,unique=True)
    pais = models.CharField(max_length=100,blank=True,null=True)
    web = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True,null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Idioma(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    FORMATO_CHOICES = [
        ('Físico', 'Físico'),
        ('Digital', 'Digital'),
        ('Audiolibro', 'Audiolibro')
    ]

    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Agotado', 'Agotado'),
        ('Próximo lanzamiento', 'Próximo lanzamiento'),
    ]
    state = models.BooleanField(default=True)
    titulo = models.CharField(max_length=255)
    volumen = models.IntegerField(blank=True,null=True)
    descripcion = models.TextField(blank = True, null = True)
    isbn = models.CharField(max_length=20, unique=True)
    imagen_portada = models.URLField(blank=False,null=False)
    fecha_publicacion = models.DateField(blank=True,null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Disponible')
    paginas = models.IntegerField(blank=True, null=True)
    formato = models.CharField(max_length=20, choices=FORMATO_CHOICES, default='Físico')
    stock = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True,blank=True)
    subcategorias = models.ManyToManyField(Subcategoria, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Imagenes(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BooleanField(default=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.URLField()

    def __str__(self):
        return f"Imagen de {self.libro.titulo}"