from django.urls import path
from notes.views.notes_views import NotesListCreateAPIView, NotesRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('notas/', NotesListCreateAPIView.as_view(), name='lista-notas'),
    path('notas/<int:pk>/', NotesRetrieveUpdateDestroyAPIView.as_view(), name='notas'),

]