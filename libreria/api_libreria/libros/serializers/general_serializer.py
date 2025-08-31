from rest_framework import serializers
from ..models import Subcategoria, Imagenes, Editorial, Categoria, Autor, Idioma

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        exclude = ('state',)

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        exclude = ('state',)

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        exclude = ('state',)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = ('state',)

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        exclude = ('state',)

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        exclude = ('state',)