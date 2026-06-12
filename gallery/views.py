from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import GalleryImage, AlbumImage
from .serializers import GalleryImageSerializer, AlbumImageSerializer
from .pagination import GalleryPagination


class GalleryListView(generics.ListAPIView):
    queryset = GalleryImage.objects.all().order_by('-created_at')
    serializer_class = GalleryImageSerializer
    pagination_class = GalleryPagination


class GalleryDetailView(generics.RetrieveAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer


class AlbumListView(generics.ListAPIView):
    queryset = AlbumImage.objects.all()
    serializer_class = AlbumImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gallery']