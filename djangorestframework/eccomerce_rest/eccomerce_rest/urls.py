
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import re_path

# Django Rest Framework Yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout, UserToken


schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v0.1',
      description="Documentación pública de API de Eccomerce",
      contact=openapi.Contact(email="leandro.carp75@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('docs/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name='Logout'),
    path('login/', Login.as_view(), name='Login'),
    path('refresh-token/',UserToken.as_view(), name='refresh_token'),
    path('users/', include('apps.users.api.urls')),
    #path('products/', include('apps.products.api.urls')),
    path('', include('apps.products.api.routers')),
    re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico'))
]
