from rest_framework import serializers
from rest_framework.validators import ValidationError
# 
from .models import UserAccount, Client, Administrator



class SignUpAdministratorSerializer(serializers.ModelSerializer):
  
  email = serializers.CharField(max_length=45)
  password = serializers.CharField(max_length=20, write_only=True)
  first_name = serializers.CharField(max_length=20)
  last_name = serializers.CharField(max_length=50)
  phone_number = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)

  class Meta:
    model = Administrator
    fields = ['id', 'email',  'password', 'first_name', 'last_name', 'phone_number', 'gender']


  def validate(self, attrs):
    email_exists = Administrator.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Administrator.objects.create(
                  email=validated_data['email'],
                  first_name = validated_data['first_name'],
                  last_name = validated_data['last_name'],
                  phone_number = validated_data['phone_number'],
                  gender = validated_data['gender'],

                    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class ClientSignUpSerializer(serializers.ModelSerializer):

  email = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, max_length=20, write_only=True)
  first_name = serializers.CharField(max_length=20)
  last_name = serializers.CharField(max_length=50)
  phone_number = serializers.CharField(max_length=20)
  gender = serializers.CharField(max_length=15)
  national = serializers.CharField(max_length=15)
  address = serializers.CharField(max_length=100)
  company_name = serializers.CharField(max_length=150)
  company_email = serializers.CharField(max_length=50)
  contactType = serializers.CharField(max_length=15)
  termsAndConditions = serializers.BooleanField(default=False)



  class Meta:
    model = Client
    fields = '__all__'
    fields = ['id', 'gender','first_name', 'last_name', 'phone_number', 'email', 'password','company_name', 'company_email',  'national', 'address', 'contactType', 'termsAndConditions']

  def validate(self, attrs):
    email_exists = Client.objects.filter(email=attrs['email']).exists()

    if email_exists:
      raise ValidationError('Email has already been used')

    return super().validate(attrs)
  
  def create(self, validated_data):
    user=Client.objects.create(
      email = validated_data['email'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      phone_number = validated_data['phone_number'],
      gender = validated_data['gender'],
      national = validated_data['national'],
      address = validated_data['address'],
      company_name = validated_data['company_name'],
      company_email = validated_data['company_email'],
      contactType = validated_data['contactType'],
      termsAndConditions=validated_data['termsAndConditions'],

    )
                                     
    user.set_password(validated_data['password'])
    user.save()

    return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'