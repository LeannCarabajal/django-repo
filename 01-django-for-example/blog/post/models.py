from django.db import models

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255,null=False,blank=False)
    slug = models.SlugField(max_length=255)
    contenido = models.TextField()
    autor = models.ForeignKey()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Autor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)