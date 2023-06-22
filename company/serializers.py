from rest_framework import serializers
from rest_framework.validators import ValidationError
from account.serializers import AccountSerializer

from .models import Company, CompanyStaff, BlogPost, Service, ClientService


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = '__all__'

class CompanyInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        exclude = ['logo']

class CompanyLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = ['logo']

class CompanyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyStaff
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields = '__all__'

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields = ['image']

class UpdateServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields = ['name', 'description']


class ClientServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientService
        fields = '__all__'