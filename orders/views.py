from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from items.models import ItemOrder, Item    
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404

class OrderViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('items')
        order_items = []
        order = Order.objects.create()

        for item_data in items:
            item = get_object_or_404(Item, id=item_data['item']['id'])
            order_items.append(ItemOrder(item=item, quantity=item_data['quantity']))

        ItemOrder.objects.bulk_create(order_items)
        order.items.add(*order_items) 
        
        return Response(OrderSerializer(order).data)
        