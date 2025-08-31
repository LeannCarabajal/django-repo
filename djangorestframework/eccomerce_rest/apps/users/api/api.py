from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer,UserListSerializer


@api_view(['GET','POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id','username','email','password')
        users_serializer = UserListSerializer(users,many=True)

    
        return Response(users_serializer.data,status= status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)

        # validation
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"message": "Usuario creado exitosamente"}, status= status.HTTP_201_CREATED) #users_serializer.data
        
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def user_detail_view(request,pk=None):
    # queryset
    user = User.objects.filter(id = pk).first()


    # validation
    if user:

        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # update   
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            try:
                user.delete()
                return Response({'status':status.HTTP_200_OK,'message':'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
            except:
                return Response('Ocurrio un problema, usuario logeado')
    return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)















#class UserAPIView(APIView):
#
 #   def get(self,request):
  #      users = User.objects.all()
   #     users_serializer = UserSerializer(users,many=True)
    #    return Response(users_serializer.data)
