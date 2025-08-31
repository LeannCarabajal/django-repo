#from rest_framework import generics
from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
#from apps.products.models import MeasureUnit,Indicator,CategoryProduct
from apps.products.models import MeasureUnit
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    
    
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer


    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return queryset

    def list(self,request):
        """Retorna todas las unidades de medidas disponibles
        
        params
        name ---> nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

class IndicatorUnitViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return queryset

class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return queryset








#class CategoryProductListAPIView(viewsets.ModelViewSet):
 #   serializer_class = CategoryProductSerializer





