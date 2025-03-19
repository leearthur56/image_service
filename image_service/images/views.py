from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Folder, Image
from .serializers import FolderSerializer, ImageSerializer, ImageListSerializer

# Create your views here.

class FolderView(APIView):
    # API endpoint that allows folders to be created
    def post(self, request):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # API endpoint that allows folders to be viewed
    def get(self, request):
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data)

class ImageView(APIView):

    # API endpoint that allows images to be uploaded
    def post(self, request, foldername):
        folder = get_object_or_404(Folder, name=foldername)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(folder=folder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # API endpoint that allows images to be viewed
    def get(self, request, foldername):
        folder = get_object_or_404(Folder, name=foldername)
        images = folder.images.all()
        serializer = ImageListSerializer(images, many=True)
        return Response(serializer.data)

class ImageDetailView(APIView):
    # API endpoint that allows a specific image to be viewed
    def get(self, request, foldername, id):
        folder = get_object_or_404(Folder, name=foldername)
        image = get_object_or_404(folder.images, id=id)
        serializer = ImageSerializer(image, context={'request': request})
        return Response(serializer.data)