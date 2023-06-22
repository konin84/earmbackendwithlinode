from django.shortcuts import render
from rest_framework import generics,status
from .models import Profile
# from account.models import UserAccount
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from .serializers import ProfileSerializer, ViewProfileSerializer

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def profileSetting(request):

  if request.method=='GET':
     data=Profile.objects.all() 
   #   data=Profile.objects.filter(accountOwner__first_name='Konyuie') 
     serializer = ViewProfileSerializer(data, many=True)
     parser_classes = (MultiPartParser, FormParser)
     respose = {'message': 'User Profile setting',
                'data': serializer.data }
     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = ProfileSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'User Profile Setting':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def userProfile (request, pk):
   try:
      data = Profile.objects.get(id=pk)
   except Profile.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = ProfileSerializer(data)
      return Response({'User': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = ProfileSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'user': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class MyProfile(generics.ListAPIView):
    permission_classes = [IsAuthenticated] # Custom permission class used~~

    queryset = Profile.objects.all()
    serializer_class = ViewProfileSerializer
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(accountOwner=user)