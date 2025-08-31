from rest_framework import serializers

from apps.products.models import Product
#from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    #measure_unit = serializers.StringRelatedField()
    #category_product = CategoryProductSerializer()
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date',)

    def to_representation(self, instance):
        info_extra = self.context.get('info_extra',None)
        info = {
            'id':instance.id,
            'name':instance.name,
            'description':instance.description,
            'imagen':instance.imagen or '',
            'measure_unit':'No especificado' if instance.measure_unit is None else instance.measure_unit.description,
            'category_product':'No especificado' if instance.category_product is None else instance.category_product.description
            }
        if info_extra:
            info['info_extra'] = info_extra
            return info
        
        return info
    
#    # def create(self,validated_data):
#     #    if validated_data['imagen'] == None:
#      #       validated_data['imagen'] = ""
#      #   return Product.objects.create(**validated_data)