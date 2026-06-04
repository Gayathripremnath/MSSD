from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gallery, Albums
from .serializers import GallerySerializer, AlbumsSerializer

class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all().order_by('-created_at')
    serializer_class = GallerySerializer

class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class AlbumListView(generics.ListAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gallery']