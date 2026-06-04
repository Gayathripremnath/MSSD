from rest_framework import serializers
from .models import Gallery, Albums


class AlbumsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Albums
        fields = ['id', 'gallery', 'image', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return f'http://127.0.0.1:8000/media/{obj.image}' if obj.image else None


class GallerySerializer(serializers.ModelSerializer):
    album_images = AlbumsSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'image_url', 'created_at', 'album_images']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return f'http://127.0.0.1:8000/media/{obj.image}' if obj.image else None
