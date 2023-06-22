# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import MyTokenObtainPairSerializer


# 
import jwt, datetime
from account.models import UserAccount
from rest_framework.exceptions import  AuthenticationFailed

# 


class MyTokenObtainPairView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
    'api/token',
    'api/token/refresh'
  ]
  return Response(routes)


class TestView(APIView):
  permission_classes = (IsAuthenticated,)

  def get(self, request):
    context = {'Hello', 'The test is working'}
    return Response(context)



class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

