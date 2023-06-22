from django.shortcuts import render
from .serializers import CompanySerializer, CompanyInfoUpdateSerializer,CompanyLogoSerializer, CompanyStaffSerializer, ServicesSerializer, ClientServicesSerializer, BlogSerializer, ServiceImageSerializer,UpdateServiceInfoSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes, APIView
#  importing models
from .models import Company, CompanyStaff, BlogPost,Service, ClientService

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser




# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def registeringCompany(request):

  if request.method=='GET':
     data=Company.objects.all() 
   #   data=Profile.objects.filter(accountOwner__first_name='Konyuie') 
     serializer = CompanySerializer(data, many=True)
    #  respose = {'message': 'Company setting',
    #             'data': serializer.data }
     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = CompanySerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'Company setting':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def companySetting (request, pk):
   try:
      data = Company.objects.get(id=pk)
   except Company.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = CompanyInfoUpdateSerializer(data)
      return Response({'Company': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = CompanyInfoUpdateSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Company': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def companyLogoSetting (request, pk):
   try:
      data = Company.objects.get(id=pk)
   except Company.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = CompanyLogoSerializer(data)
      return Response({'Company': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = CompanyLogoSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'Company': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
        



# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def newBlob(request):

  if request.method=='GET':
     data=BlogPost.objects.all() 
   #   data=Profile.objects.filter(accountOwner__first_name='Konyuie') 
     serializer = BlogSerializer(data, many=True)
    #  respose = {'message': 'Company setting',
    #             'data': serializer.data }
     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = BlogSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'new blog':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def blog (request, slug):
   try:
      data = BlogPost.objects.get(slug=slug)
   except BlogPost.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = BlogSerializer(data)
      return Response({'blog': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = BlogSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'blog': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def services(request):

  if request.method=='GET':
     data=Service.objects.all() 
   #   data=Profile.objects.filter(accountOwner__first_name='Konyuie') 
     serializer = ServicesSerializer(data, many=True)
    #  respose = {'message': 'Company setting',
    #             'data': serializer.data }
     return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    serialiazer = ServicesSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response({'services':serialiazer.data}, status=status.HTTP_200_OK)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
  


@api_view(['GET'])
def allservices(request):
      
     data=Service.objects.all() 
   #   data=Profile.objects.filter(accountOwner__first_name='Konyuie') 
     serializer = ServicesSerializer(data, many=True)
    #  respose = {'message': 'Company setting',
    #             'data': serializer.data }
     return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def allBlogs(request):
     data=BlogPost.objects.all() 
     serializer = BlogSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def publishedBlogs(request):
      
     data=BlogPost.objects.filter(published=True) 
     serializer = BlogSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def singlePublishedBlog(request, slug):
     try:
      data = BlogPost.objects.get(slug=slug)
     except BlogPost.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method=='GET':
      serialiazer = BlogSerializer(data)
      return Response({'blog': serialiazer.data}, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def service (request, slug):
   try:
      data = Service.objects.get(slug=slug)
   except Service.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = ServicesSerializer(data)
      return Response({'service': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = UpdateServiceInfoSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'service': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def singleService(request, slug):
     try:
      data = Service.objects.get(slug=slug)
     except Service.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method=='GET':
      serialiazer = ServicesSerializer(data)
      return Response({'service': serialiazer.data}, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def serviceImageSetting (request, slug):
   try:
      data = Service.objects.get(slug=slug)
   except Service.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method=='GET':
      serialiazer = ServiceImageSerializer(data)
      return Response({'service': serialiazer.data}, status=status.HTTP_200_OK)
   
   elif request.method == 'DELETE':
      data.delete()
      return Response(status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serialiazer = ServiceImageSerializer(data, data=request.data)
      if serialiazer.is_valid():
         serialiazer.save()
         return Response({'service': serialiazer.data}, status=status.HTTP_200_OK)
      return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

