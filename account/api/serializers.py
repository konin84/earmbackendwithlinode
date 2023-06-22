from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from account.models import UserAccount

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['id'] = user.id
        token['email'] = user.email
        token['role'] = user.role
        token['first_name'] = user.first_name 
        token['last_name'] = user.last_name  
        token['phone_number'] = user.phone_number 
        # token['houserented'] = user.houserented 
        # ...

        return token
