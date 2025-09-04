from rest_framework import generics
from ..models import Evento
from ..serializers.evento_serializer import EventoSerializer

class EventoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
