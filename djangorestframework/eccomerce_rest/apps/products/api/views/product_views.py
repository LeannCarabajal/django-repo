from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.users.authentication_mixins import Authentication
from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.products.models import Product


class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def not_found(self):
        return Response({"error":"No existe un producto con estos datos"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    def list(self,request):
        # Parse query parameters
        nombre = request.query_params.get('name')
        categoria = request.query_params.get('category')
            
        # Filter queryset
        queryset = self.get_queryset()
        if nombre and categoria:
            queryset = queryset.filter(name=nombre, category_product__description = categoria)
        elif categoria:
            queryset = queryset.filter(category_product__description = categoria)
        elif nombre:
            queryset = queryset.filter(name=nombre)
            

        # Serialize and return data
        serializer = self.serializer_class(queryset, many = True, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print("data validada")
            serializer.save()
            return Response({"Message":"Producto Creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        product = self.get_queryset(pk)    
        print("Destroy method")
        if product:
            product.state = False
            product.save()
            return Response({'message':"Producto Eliminado Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()

    def update(self,request,pk=None):
        product = self.get_queryset(pk)
        print("Update Method")
        if product:
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()










































"""
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self,request):
        # Parse query parameters
        nombre = request.query_params.get('name')
        categoria = request.query_params.get('category')
        
        # Filter queryset
        queryset = self.get_queryset()
        if nombre and categoria:
            queryset = queryset.filter(name=nombre, category_product__description = categoria)
        elif categoria:
            queryset = queryset.filter(category_product__description = categoria)
        elif nombre:
            queryset = queryset.filter(name=nombre)
        

        # Serialize and return data
        serializer = self.serializer_class(queryset, many = True, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print("data validada")
            serializer.save()
            return Response({"Message":"Producto Creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def not_found(self):
        return Response({"error":"No existe un producto con estos datos"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
            if pk is None:
                return self.get_serializer().Meta.model.objects.filter(state=True)
            else:
                return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def get(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            serializer = self.serializer_class(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        product = self.get_queryset(pk)    
        if product:
            product.state = False
            product.save()
            return Response({'message':"Producto Eliminado Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()




































class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            serializer = self.serializer_class(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
    #def get(self,request,pk=None)
""""""
#Eliminación Por Estado
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        #model = Product
        # Este código busca y obtiene el modelo especificado en la clase Meta del serializador asociado a la vista.
        model = self.get_serializer().Meta.model
        # Retorna el conjunto de objetos (model.objects) filtrado por la condición state=True
        return model.objects.filter(state = True) # Retorna el modelo filtrado por estado verdadero

    def delete(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':"Producto Eliminado Correctamente"},status=status.HTTP_200_OK)
        return Response({"error":"No existe un producto con estos datos"},status=status.HTTP_404_NOT_FOUND)
"""
"""
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True) #return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get_object(self,pk):
        return self.get_queryset().filter(id=pk).first()    

    def not_found(self):
        return Response({"error":"No existe un producto con estos datos"},status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk=None):
        product = self.get_object(pk)
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product_serializer = ProductSerializer(product, data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
"""


"""
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['info_extra'] = 'Hola, esto es información extra'
        return context
    def get(self,request):
        # Pasa 'many=True' para indicar que es una lista de objetos, no un solo objeto
        serializer = self.serializer_class(self.get_queryset(), many=True, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)
"""
       
#class ProductCreateAPIView(generics.CreateAPIView):"""