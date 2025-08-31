from rest_framework import serializers
from libros.models import Libro, Imagenes
from .general_serializer import *

class LibroSerializer(serializers.ModelSerializer):
    imagenes = serializers.ListField(
        child=serializers.URLField(), write_only=True, required=False
    )

    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), required=True)
    editorial = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all(), required=True)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all(), required=True)
    subcategorias = serializers.PrimaryKeyRelatedField(queryset=Subcategoria.objects.all(), many=True, required=False)
    idioma = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Libro
        fields = [
            'id', 'titulo', 'volumen', 'descripcion', 'isbn', 'imagen_portada',
            'fecha_publicacion', 'estado', 'editorial', 'paginas', 'formato', 'stock', 'creado', 'actualizado',
            'autor', 'idioma', 'categoria', 'subcategorias', 'imagenes' 
        ]
    
    def create(self, validated_data):
        # Extraer imágenes del payload
        imagenes_data = validated_data.pop('imagenes', [])
        subcategorias_data = validated_data.pop('subcategorias', [])
        libro = Libro.objects.create(**validated_data)
        
        libro.subcategorias.set(subcategorias_data)
        
        for imagen_url in imagenes_data:
            Imagenes.objects.create(libro=libro, imagen=imagen_url)

        return libro
    
    def get_idioma(self, obj):
        return {"id":obj.idioma.id, "nombre":obj.idioma.nombre} if obj.idioma else None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['imagenes'] = [img.imagen for img in instance.imagenes.all()]
        representation['categoria'] = CategoriaSerializer(instance.categoria).data if instance.categoria else None
        representation['editorial'] = EditorialSerializer(instance.editorial).data if instance.editorial else None
        representation['autor'] = AutorSerializer(instance.autor).data if instance.autor else None
        representation['subcategorias'] = SubcategoriaSerializer(instance.subcategorias.all(), many=True).data
    
        return representation