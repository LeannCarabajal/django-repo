from django.urls import path


from api.views.sala_view import SalaListCreateAPIView, SalaRetrieveUpdateDestroyAPIView
from api.views.baliza_view import BalizaListCreateAPIView, BalizaRetrieveUpdateDestroyAPIView
from api.views.evento_view import EventoListCreateAPIView
from api.views.sesion_view import SesionListAPIView

urlpatterns = [
    path('salas/', SalaListCreateAPIView.as_view(), name='lista-salas'),
    path('salas/<int:pk>/', SalaRetrieveUpdateDestroyAPIView.as_view(), name='sala'),
    path('balizas/', BalizaListCreateAPIView.as_view(), name='lista-balizas'),
    path('balizas/<int:pk>/', BalizaRetrieveUpdateDestroyAPIView.as_view(), name='baliza'),
    path('eventos/', EventoListCreateAPIView.as_view(), name='lista-eventos'),
    path('sesiones/', SesionListAPIView.as_view(), name='lista-sesiones'),

]