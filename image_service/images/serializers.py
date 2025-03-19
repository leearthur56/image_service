from rest_framework import serializers
from .models import Folder, Image
from PIL import Image as PILImage
from django.core.files.storage import default_storage

class FolderSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Folder
        fields = ['id', 'name', 'created_at']

class ImageSerializer(serializers.ModelSerializer):
    # Define additional fields that are not directly present in the model
    folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all(), required=False)
    image_url = serializers.SerializerMethodField()

    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Image
        fields = ['id', 'folder', 'image', 'uploaded_at', 'image_width', 'image_height', 'file_size', 'is_color', 'image_url']

    # Method to get the image URL
    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url

    # Method to create an image instance
    def create(self, validated_data):
        image_instance = super().create(validated_data)

        # Open the image file
        with default_storage.open(image_instance.image.name, 'rb') as file:
            img = PILImage.open(file)
            width, height = img.size
            file_size = image_instance.image.size  # File size in bytes
            is_color = img.mode in ("RGB", "RGBA")  # Determine if the image is color or grayscale

        # Update the instance with calculated metadata
        image_instance.image_width = width
        image_instance.image_height = height
        image_instance.file_size = file_size
        image_instance.is_color = is_color
        image_instance.save(update_fields=["image_width", "image_height", "file_size", "is_color"])

        return image_instance

class ImageListSerializer(serializers.ModelSerializer):
    # Define additional fields that are not directly present in the model
    image = serializers.SerializerMethodField()

    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Image
        fields = ['id', 'image']

    # Method to get the image URL
    def get_image(self, obj):
        return obj.image.urlc