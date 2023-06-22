from django.shortcuts import render
from .models import Photo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PhotoSerializer



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def photos(request):

  if request.method=='GET':
     data=Photo.objects.all() 
     serializer = PhotoSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_201_CREATED)
  
  elif request.method == 'POST':
    serialiazer = PhotoSerializer(data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()

      return Response({'photo':serialiazer.data}, status=status.HTTP_201_CREATED)
    return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def photo(request, pk):
    try:
        data = Photo.objects.get(id=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_200_OK)

    if request.method == 'GET':
        serialiazer = PhotoSerializer(data)
        return Response({'photo': serialiazer.data}, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    elif request.method == 'PUT':
        serialiazer = PhotoSerializer(data, data=request.data)
        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'photo': serialiazer.data}, status=status.HTTP_200_OK)
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def allPhoto(request):
     data=Photo.objects.all() 
     serializer = PhotoSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def publishedPhotos(request):
     data=Photo.objects.filter(published=True) 
     serializer = PhotoSerializer(data, many=True)
     return Response(data=serializer.data, status=status.HTTP_200_OK)



