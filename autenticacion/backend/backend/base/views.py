from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Nota
from .serializer import NotaSerializer, UserRegistrationSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self,request,*args,**kwargs):
        try:
            response = super().post(request,*args,**kwargs)
            tokens = response.data
            
            access_token = tokens['access']
            refresh_token = tokens['refresh']

            res = Response()

            res.data = {"success":True}

            res.set_cookie(
                key = "access_token",
                value = access_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
                )
            
            res.set_cookie(
                key = "refresh_token",
                value = refresh_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
                )

            return res

        except:
            return Response({"success":False})
        
class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            
            request.data['refresh'] = refresh_token

            response = super().post(request, *args, **kwargs)

            tokens = response.data
            
            access_token = tokens['access']
            res = Response()

            res.data = {'refreshed':True}

            res.set_cookie(
                key = "access_token",
                value = access_token,
                httponly = True,
                secure = True,
                samesite = 'None',
                path = '/'
            )
            
            return res

        except:
            return Response({'refreshed':False})


class Logout(APIView):
    def post(self,request,*args,**kwargs):
        try:
            res = Response()
            res.data = {"success":True}
            res.delete_cookie('access_token', path='/', samesite='None')
            res.delete_cookie('refresh_token', path='/', samesite='None')
            return res
        
        except:
            return Response({"success":False})
        

class Authenticated(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')
        return Response({'authenticated':True, 'tokens':{"access_token":access_token,"refresh_token":refresh_token}})

class Register(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NotasListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Nota.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        notas = self.get_queryset()
        serializer = self.get_serializer(notas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({"message": "Nota creada correctamente", "nota": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













# class NotasListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = NotaSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         """Retorna solo las notas del usuario autenticado."""
#         return self.get_serializer().Meta.model.objects.filter(owner=self.request.user)

#     def perform_create(self, serializer):
#         """Asigna el usuario autenticado como dueño de la nota antes de guardarla."""
#         serializer.save(owner=self.request.user)






# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_notas(request):
#     user = request.user
#     notas = Nota.objects.filter(owner=user)
#     serializer = NotaSerializer
#     return Response(serializer.data)