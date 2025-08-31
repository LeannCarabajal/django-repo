from django.urls import path
from libros.views.book_views import LibroListCreateAPIView, LibroRetrieveUpdateDestroyAPIView
from libros.views.autor_views import AutorListCreateAPIView, AutorRetrieveUpdateDestroyAPIView
from libros.views.categoria_views import CategoriaListCreateAPIView, CategoriaRetrieveUpdateDestroyAPIView
from libros.views.subcategoria_view import SubcategoriaListCreateAPIView, SubcategoriaRetrieveUpdateDestroyAPIView
from libros.views.editorial_view import EditorialListCreateAPIView, EditorialRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('libros/', LibroListCreateAPIView.as_view(), name='lista-libros'),
    path('libros/<int:pk>/', LibroRetrieveUpdateDestroyAPIView.as_view(), name='libro'),
    path('autores/', AutorListCreateAPIView.as_view(), name='lista-autores'),
    #path('autores', AutorListCreateAPIView.as_view(), name='lista-autores-sin-slash'),
    path('autores/<int:pk>', AutorRetrieveUpdateDestroyAPIView.as_view(), name='autor'),
    path('categorias/', CategoriaListCreateAPIView.as_view(), name="lista-categorias"),
    path('categorias/<int:pk>', CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='categoria'),
    path('subcategorias/', SubcategoriaListCreateAPIView.as_view(), name='lista-subcategorias'),
    path('subcategorias/<int:pk>', SubcategoriaRetrieveUpdateDestroyAPIView.as_view(), name='subcategoria'),
    path('editoriales/', EditorialListCreateAPIView.as_view(), name='lista-editoriales'),
    path('editoriales/<int:pk>', EditorialRetrieveUpdateDestroyAPIView.as_view(), name='editorial')
]