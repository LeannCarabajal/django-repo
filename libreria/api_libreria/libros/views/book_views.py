from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from libros.models import Libro
from ..serializers.book_serializer import LibroSerializer

class LibroListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LibroSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def get(self, request):
        categoria = request.query_params.get('categoria')
        titulo = request.query_params.get('titulo')
        if categoria and titulo:
            libro = self.get_queryset().filter(categoria__nombre__icontains=categoria, titulo__icontains=titulo)
        elif categoria:
            libro = self.get_queryset().filter(categoria__nombre__icontains=categoria)
        elif titulo:
            libro = self.get_queryset().filter(titulo__icontains=titulo)
        else:
            libro = self.get_queryset()
        if libro:
            serializer = self.serializer_class(libro, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"No se han encontrado libros"},status=status.HTTP_404_NOT_FOUND)

class LibroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    
    def get_queryset(self):
        queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return queryset
    
    def get_libro(self, pk=None):
        return self.get_queryset().filter(id=pk).first() or self.get_queryset().filter(isbn=pk).first()
    
    def not_found(self):
        return Response({"error":"Libro no encontrado"},status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk=None):
        libro = self.get_libro(pk)
        if libro:
            serializer = self.serializer_class(libro)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()
    
    def patch(self,request,pk=None):
        libro = self.get_libro(pk) 
        if libro:
            serializer = self.serializer_class(libro)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return self.not_found()
    
    def put(self,request,pk=None):
        libro = self.get_libro(pk)
        if libro:
            serializer = self.serializer_class(self.get_libro(pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.not_found()
    def destroy(self,request,pk=None):
        libro = self.get_libro(pk)
        if libro:
            libro.state = False
            libro.save()
            return Response({'message':"Libro Eliminado Correctamente"},status=status.HTTP_200_OK)
        return self.not_found()