from rest_framework import serializers
from apps.users.models import User




class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'                      #('id','username','email','password') #['name','last_name']

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def to_representation(self, instance):
        """print(instance)
        data = super().to_representation(instance)
        print(data)"""
        return {
            'id':instance['id'],
            'username':instance['username'],
            'email':instance['email'],
            'password':instance['password']
        }

    











"""
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    is_superuser = serializers.BooleanField()
    password = serializers.CharField(max_length=250)


    def validate_name(self, value):
        # custom validation
        if 'developer' in value:
            #print(serializers.ValidationError('Error, no puede existir un usuario con ese nombre'))
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        

        return value

    def validate_email(self, value):
        # custom validation
        if value == '':
            raise serializers.ValidationError('Error, tiene que colocar un correo')
        
       # if self.validate_name(self.context['name']) in value:
        #    raise serializers.ValidationError("El email no puede contener el nombre")
        return value
    
    def validate(self,data):
        #print(data)
        return data
    
    def validate_is_superuser(self, value):
        return value
    
    def create(self,validated_data):
        print(validated_data)

        return User.objects.create(**validated_data)
    

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password',instance.password)
        instance.is_superuser = validated_data.get('is_superuser',instance.is_superuser)
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
    #def save(self):
    #    print(self.validated_data)















test_data = {
            'name':'develop',
            'email':'dev3loper@gmail.com'

        }
        test_user = TestUserSerializer(data = test_data, context = test_data)

        if test_user.is_valid():
            user_instance = test_user.save()
            print(user_instance)
        else:
            print(test_user.errors)
"""