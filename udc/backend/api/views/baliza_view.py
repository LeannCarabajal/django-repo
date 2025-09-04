from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.models import Baliza
from api.serializers.general_serializer import BalizaSerializer

class BalizaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BalizaSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron balizas"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):

        categoria = self.get_queryset()
            
        serializer = self.serializer_class(categoria, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class BalizaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BalizaSerializer

    def not_found(self):
        return Response({"error":"No se encontro una baliza con ese ID"})
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
        
    def get(self, request, pk=None):
        baliza = self.get_queryset(pk)
        if baliza:
            serializer = self.serializer_class(baliza)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()       
    
    def patch(self,request,pk=None):
        baliza = self.get_queryset(pk)
        if baliza:
            serializer = self.serializer_class(baliza)
            return Response(serializer.data,status = status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        baliza = self.get_queryset(pk)
        if baliza:
            serializer = self.serializer_class(baliza, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    
    def destroy(self,request,pk=None):
        baliza = self.get_queryset(pk)    
        if baliza:
            baliza.state = False
            baliza.save()
            return Response({'message':"Baliza eliminada correctamente"},status=status.HTTP_200_OK)
        return self.not_found()