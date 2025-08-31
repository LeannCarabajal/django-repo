from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from libros.models import Categoria
from libros.serializers.general_serializer import CategoriaSerializer

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategoriaSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron categorias"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):
        nombre = request.query_params.get('nombre')

        if nombre:
            categoria = self.get_queryset().filter(nombres__icontains = nombre)
        else:
            categoria = self.get_queryset()
            
        if categoria:
            serializer = self.serializer_class(categoria, many = True, context=self.get_serializer_context())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()  


class CategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriaSerializer

    def not_found(self):
        return Response({"error":"No existe una categoría con ese ID"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
            if pk is None:
                return self.get_serializer().Meta.model.objects.filter(state=True)
            else:
                return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
            
    def get(self, request, pk=None):
        categoria = self.get_queryset(pk)
        if categoria:
            serializer = self.serializer_class(categoria)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        categoria = self.get_queryset(pk)
        if categoria:
            serializer = self.serializer_class(categoria)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        categoria = self.get_queryset(pk)
        if categoria:
            serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        categoria = self.get_queryset(pk)    
        if categoria:
            categoria.state = False
            categoria.save()
            return Response({'message':"Categoría Eliminada Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()


