from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .serializers import ClientSignUpSerializer, SignUpAdministratorSerializer, AccountSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes, APIView
#  importing models
from .models import UserAccount, Client, Administrator

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from .permissions import IsAdmin, IsRealtor, IsHouseOwner, IsTenant
from rest_framework import generics
#
from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from earm.settings import EMAIL_HOST_USER



class ClientSignUp(generics.CreateAPIView):
    serializer_class = ClientSignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            # EMAIL SETTING
            subject = 'Interested Company'
            message = "Dear, " + data['first_name'] + " " + data['last_name'] + " representing " + \
                data['company_name'] + ". " \
                    + "Thanks for showing your interest with us, we will exchange with you and proceed." + \
                " " + "Your password is: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)

            # END OF SETTING
            print('User Email: ', email)
            print('Company Message: ', message)
            # print('Company Name: ', data['com'])

            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpAdministrator(generics.CreateAPIView):
    serializer_class = SignUpAdministratorSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():

            subject = 'Aministrator Account Creation'
            message = "Dear Landlord," + " " + \
                data['firt_name'] + " " + data['last_name'] + ". " + \
                "Your account to use this service has been created" + \
                " " + "Your password is: " + data['password']

            email = data['email']
            recipient_list = [email]

            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently=True)
            
            print('User Email: ', email)
            print('Company Message: ', message)
            
            serializer.save()
            response = {
                "message": "User created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def allUsers(request):
    # Querying Employees table/model
    users = UserAccount.objects.all()
    # Converting the Employees query into json
    serializer = AccountSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def allClients(request):
    clients = Client.objects.all()
    # Converting the Employees query into json
    serializer = AccountSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def client(request, pk):
    try:
        data = Client.objects.get(id=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = AccountSerializer(data)
        return Response({'client': serialiazer.data}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = AccountSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'client': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
