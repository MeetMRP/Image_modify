from rest_framework import  serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','email','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = user.objects.create_user(validated_data['email'],     
                                        password = validated_data['password'],
                                        first_name=validated_data['first_name'],  
                                        last_name=validated_data['last_name'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = ['id', 'image']
        extra_kwargs = {
            'image':{'write_only': True},
        }