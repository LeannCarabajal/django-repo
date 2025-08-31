from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from libros.models import Autor
from libros.serializers.general_serializer import AutorSerializer

class AutorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = AutorSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron autores"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):
        nombres = request.query_params.get('nombres')
        apellido = request.query_params.get('apellido')

        if nombres and apellido:
            autores = self.get_queryset().filter(nombres__icontains = nombres, apellido__icontains = apellido)
        elif nombres:
            autores = self.get_queryset().filter(nombres__icontains = nombres)
        elif apellido:
            autores = self.get_queryset().filter(apellido__icontains = apellido)
        else:
            autores = self.get_queryset()
        if autores:
            serializer = self.serializer_class(autores, many = True, context=self.get_serializer_context())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()  


class AutorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AutorSerializer

    def not_found(self):
        return Response({"error":"No existe un autor con ese ID"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
            if pk is None:
                return self.get_serializer().Meta.model.objects.filter(state=True)
            else:
                return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
            
    def get(self, request, pk=None):
        autor = self.get_queryset(pk)
        if autor:
            serializer = self.serializer_class(autor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        autor = self.get_queryset(pk)
        if autor:
            serializer = self.serializer_class(autor)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        autor = self.get_queryset(pk)
        if autor:
            serializer = self.serializer_class(autor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        autor = self.get_queryset(pk)    
        if autor:
            autor.state = False
            autor.save()
            return Response({'message':"Autor Eliminado Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()


