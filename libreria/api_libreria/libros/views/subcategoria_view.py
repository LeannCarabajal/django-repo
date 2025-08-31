from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from libros.models import Subcategoria
from libros.serializers.general_serializer import SubcategoriaSerializer

class SubcategoriaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubcategoriaSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron subcategorias"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):
        nombre = request.query_params.get('nombre')

        if nombre:
            subcategoria = self.get_queryset().filter(nombres__icontains = nombre)
        else:
            subcategoria = self.get_queryset()
            
        if subcategoria:
            serializer = self.serializer_class(subcategoria, many = True, context=self.get_serializer_context())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()  


class SubcategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubcategoriaSerializer

    def not_found(self):
        return Response({"error":"No existe una subcategoría con ese ID"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
            if pk is None:
                return self.get_serializer().Meta.model.objects.filter(state=True)
            else:
                return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
            
    def get(self, request, pk=None):
        subcategoria = self.get_queryset(pk)
        if subcategoria:
            serializer = self.serializer_class(subcategoria)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        subcategoria = self.get_queryset(pk)
        if subcategoria:
            serializer = self.serializer_class(subcategoria)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        subcategoria = self.get_queryset(pk)
        if subcategoria:
            serializer = self.serializer_class(subcategoria, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        subcategoria = self.get_queryset(pk)    
        if subcategoria:
            subcategoria.state = False
            subcategoria.save()
            return Response({'message':"Categoría Eliminada Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()


