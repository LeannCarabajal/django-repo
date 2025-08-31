from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from libros.models import Editorial
from libros.serializers.general_serializer import EditorialSerializer

class EditorialListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EditorialSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron editoriales"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):
        nombre = request.query_params.get('nombre')

        if nombre:
            editorial = self.get_queryset().filter(nombre__icontains = nombre)
        else:
            editorial = self.get_queryset()
            
        if editorial:
            serializer = self.serializer_class(editorial, many = True, context=self.get_serializer_context())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()  


class EditorialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditorialSerializer

    def not_found(self):
        return Response({"error":"No existe una editorial con ese ID"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self, pk=None):
         return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
            
    def get(self, request, pk=None):
        editorial = self.get_queryset(pk)
        if editorial:
            serializer = self.serializer_class(editorial)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        editorial = self.get_queryset(pk)
        if editorial:
            serializer = self.serializer_class(editorial)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        editorial = self.get_queryset(pk)
        if editorial:
            serializer = self.serializer_class(editorial, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        editorial = self.get_queryset(pk)    
        if editorial:
            editorial.state = False
            editorial.save()
            return Response({'message':"Editorial eliminada correctamente"},status=status.HTTP_200_OK)
        return self.not_found()


