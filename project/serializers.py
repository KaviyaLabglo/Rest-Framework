from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers


# accounts/api/serializers.py

from django.contrib.auth import authenticate
from project.models import *
from django.contrib.auth.models import User

from rest_framework import serializers




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields ="__all__"

# Serializer to Get User Details using Django Token Authentication

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_user_token')
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password","token"]
        
    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key
    
    
    
    
        
# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=True)
    
    token = serializers.SerializerMethodField('get_user_token')
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'token')
        
        

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key
