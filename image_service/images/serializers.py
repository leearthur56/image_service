from rest_framework import serializers
from .models import Folder, Image

class FolderSerializer(serializers.ModelSerializer):
    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Folder
        fields = ['id', 'name', 'created_at']

class ImageSerializer(serializers.ModelSerializer):
    # Define additional fields that are not directly present in the model
    folder = serializers.PrimaryKeyRelatedField(queryset=Folder.objects.all(), required=False)
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    file_size = serializers.SerializerMethodField()
    is_color = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Image
        fields = ['id', 'folder', 'image', 'uploaded_at', 'width', 'height', 'file_size', 'is_color', 'image_url']

    # Method to get the width of the image
    def get_width(self, obj):
        return obj.get_image_size()[0]

    # Method to get the height of the image
    def get_height(self, obj):
        return obj.get_image_size()[1]

    # Method to get the file size of the image
    def get_file_size(self, obj):
        return obj.get_file_size()

    # Method to check if the image is in color
    def get_is_color(self, obj):
        return obj.is_color_image()

    # Method to get the image URL
    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url

class ImageListSerializer(serializers.ModelSerializer):
    # Define additional fields that are not directly present in the model
    image = serializers.SerializerMethodField()

    # Meta class to specify the model and fields to be serialized
    class Meta:
        model = Image
        fields = ['id', 'image']

    # Method to get the image URL
    def get_image(self, obj):
        return obj.image.url