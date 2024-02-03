from rest_framework import serializers
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(serializers.ModelSerializer):
    image_path = VersatileImageFieldSerializer("primary_image_detail")
    class Meta:
        model = Image
        fields = 'image_path'