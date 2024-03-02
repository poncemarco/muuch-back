from rest_framework import serializers
from .models import Image
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ImageSerializer(serializers.ModelSerializer):
    image_path = VersatileImageFieldSerializer(
        sizes = [
            ('primary', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )
    class Meta:
        model = Image
        fields = ['image_path']