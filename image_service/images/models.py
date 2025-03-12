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

    def __str__(self):
        # Return the name of the image file
        return self.image.name

    def get_image_size(self):
        # Get the dimensions of the image
        with PILImage.open(self.image.path) as img:
            return img.size

    def get_file_size(self):
        # Get the size of the image file in bytes
        return self.image.size

    def is_color_image(self):
        # Check if the image is in color (RGB or RGBA mode)
        from PIL import Image as PILImage
        with PILImage.open(self.image.path) as img:
            return img.mode in ('RGBA', 'RGB')