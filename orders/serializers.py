from rest_framework import serializers
from .models import Order
from items.serializers import ItemOrderSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = ItemOrderSerializer(many=True, write_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'

        
