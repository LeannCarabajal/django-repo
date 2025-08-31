from rest_framework import generics, status
from rest_framework.response import Response
from notes.models import Notas
from notes.serializers.notes_serializer import NotesSerializer


class NotesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):
        notas = self.get_queryset()

        if notas: 
            serializer = self.serializer_class(notas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"No se han encontrado notas"},status=status.HTTP_404_NOT_FOUND)
    
class NotesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notas.objects.all()
    serializer_class = NotesSerializer

    
    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return queryset
    
    def get_nota(self, pk=None):
        return self.get_queryset().filter(id=pk).first()
    
    def not_found(self):
        return Response({"error":"Nota no encontrado"},status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk=None):
        nota = self.get_nota(pk)
        if nota:
            serializer = self.serializer_class(nota)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()
    
    def patch(self,request,pk=None):
        nota = self.get_nota(pk) 
        if nota:
            serializer = self.serializer_class(nota)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        nota = self.get_nota(pk)
        if nota:
            serializer = self.serializer_class(self.get_nota(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    def destroy(self,request,pk=None):
        nota = self.get_nota(pk)
        if nota:
            nota.state = False
            nota.save()
            return Response({'message':"Nota Eliminada Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()