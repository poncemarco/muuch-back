from rest_framework import serializers
from .models import Item, RequestItem, ItemOrder
from files.serializers import ImageSerializer

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    price = serializers.FloatField()
    
    def get_image(self, obj):
        return str(obj.images.first().image_path) if obj.images.first() else None
    
    class Meta:
        model = Item
        fields = ["id" ,"name", "unit", "category", "price", "image" ]
        
class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = ItemOrder
        fields = ["item", "quantity"]

class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = "__all__"
        