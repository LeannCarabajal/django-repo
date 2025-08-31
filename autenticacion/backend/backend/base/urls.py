from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path

from .views import NotasListCreateAPIView, CustomTokenObtainPairView
from .views import CustomRefreshTokenView, Logout, Authenticated, Register

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('notas/', NotasListCreateAPIView.as_view(), name="notas"),
    path('logout/', Logout.as_view(), name="logout"),
    path('authenticated/', Authenticated.as_view(), name="authenticated"),
    path('register/', Register.as_view(), name="register")
]