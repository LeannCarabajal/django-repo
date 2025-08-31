from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoría', max_length = 100, blank = False, null = False)
    estado = models.BooleanField('Categiría Activada/Categoría no Activada', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres del Autor', max_length=255,null=False,blank=False)
    apellidos = models.CharField('Apellido del Autor',max_length=255,null=False,blank=False)
    facebook = models.URLField('Facebook',null=True,blank=True)
    twitter = models.URLField('Twitter',null=True,blank=True)
    instagram = models.URLField('Instagram',null=True,blank=True)
    web = models.URLField('Web',null=True,blank=True)
    correo = models.EmailField('Correo electrónico',null=False,blank=False)
    estado = models.BooleanField('Autor Activo/No Activo',default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0} {1}".format(self.nombres,self.apellidos)
    

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título',max_length=90,blank=False,null=False)
    slug = models.CharField('Slug',max_length=100,blank=False,null=False)
    descripcion = models.CharField('Descripción',max_length=110,blank=False,null=False) 
    contenido = CKEditor5Field('Text', config_name='extends')
    imagen = models.URLField(max_length=255,blank=False,null=False)   
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo