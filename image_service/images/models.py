from django.db import models
from PIL import Image as PILImage

# Create your models here.

class Folder(models.Model):
    # The name of the folder, must be unique
    name = models.CharField(max_length=255, unique=True)
    # The date and time when the folder was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the name of the folder
        return self.name

class Image(models.Model):
    # The folder to which the image belongs, with a cascade delete behavior
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='images')
    # The image file
    image = models.ImageField(upload_to='uploads/')
    # The date and time when the image was uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image_width = models.IntegerField(null=True)
    image_height = models.IntegerField(null=True)
    file_size = models.IntegerField(null=True)
    is_color = models.BooleanField(null=True)

    def __str__(self):
        # Return the name of the image file
        return self.image.name