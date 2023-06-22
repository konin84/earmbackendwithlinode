from rest_framework import serializers
from rest_framework.validators import ValidationError
from account.serializers import *

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # accountOwner = AccountSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        
class ViewProfileSerializer(serializers.ModelSerializer):
    accountOwner = AccountSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

