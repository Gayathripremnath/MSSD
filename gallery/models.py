from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_image(file):
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png']

    if ext not in valid_extensions:
        raise ValidationError("Only JPG and PNG files are allowed!")

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/', validators=[validate_image])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Albums(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='album_images', null=True, blank=True)
    image = models.ImageField(upload_to='gallery/', validators=[validate_image])

    def __str__(self):
        return f"AlbumImage for {self.gallery.title if self.gallery else 'Orphaned'}"
    
