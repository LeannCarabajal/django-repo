from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.models import Sesion
from api.serializers.general_serializer import SesionSerializer

class SesionListAPIView(generics.ListAPIView):
    serializer_class = SesionSerializer
    
    def not_found(self):
        return Response({"error":"No se encontraron sesiones"},status=status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def get(self, request):

        categoria = self.get_queryset()
            
        serializer = self.serializer_class(categoria, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

