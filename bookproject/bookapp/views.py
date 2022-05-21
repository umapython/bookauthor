from django.shortcuts import render
from rest_framework import  serializers
from .serializers import RegisterSerializer,Book_detailSerializer,LoginSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.permissions import AllowAny
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def Register(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    serializer=LoginSerializer(data=request.data)
    return(request.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def BooksAuthor(request):
    serializer=Book_detailSerializer(comment)
    if serializer.data():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_created)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)