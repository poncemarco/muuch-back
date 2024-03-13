from rest_framework import serializers
from .models import Item, RequestItem, ItemOrder, Category
from files.serializers import ImageSerializer

class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    
    def get_price(self, obj):
        return obj.price_display()
    
    def get_category(self, obj):
        return obj.category.name
    
    def get_image(self, obj):
        image = obj.images.first()
        if image:
            return ImageSerializer(image).data
        return None
    
    def get_slug(self, obj):
        return obj.slug()
    
    class Meta:
        model = Item
        fields = ["id" ,"name", "unit", "category", "price", "image", "slug"]
        
class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = ItemOrder
        fields = ["item", "quantity"]

class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    number_of_items = serializers.SerializerMethodField()
    
    def get_number_of_items(self, obj):
        return obj.item_set.count()
    
    class Meta:
        model = Category
        fields = ["id", "name", "number_of_items"]
        