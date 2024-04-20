from rest_framework import viewsets
from .models import Order, DiscountCode
from .serializers import OrderSerializer
from rest_framework.response import Response
from items.models import ItemOrder, Item, RequestItem
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404
from .functions import TicketManager
from orders.functions import WhatsappManager
from django.contrib.auth.models import User
from users.models import Phone, Address
from locations.models import Zones


class OrderViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('items')
        name = request.data.pop('name')
        email = request.data.pop('email')
        phone = request.data.pop('phone')
        outter_items = request.data.pop('outterItems')
        address = request.data.pop('address')
        user, is_new_user = User.objects.get_or_create(email=email, username=email)
        Phone.objects.get_or_create(user=user, phone=phone)
        zone = Zones.objects.filter(neighborhood__name=address['neighborhood']).first()
        if zone:
            Address.objects.get_or_create(user=user, street=address['street'],  zone=zone, particular_reference=address['complement'])
        discount = None
        if 'couppon' in request.data:
            try:
                discount = DiscountCode.objects.get(code=request.data['couppon'])
            except DiscountCode.DoesNotExist:
                pass
        order_items = []
        order = Order.objects.create(discount=discount, user=user)

        for item_data in items:
            item = get_object_or_404(Item, id=item_data['id'])
            order_items.append(ItemOrder(item=item, quantity=item_data['quantity']))

        ItemOrder.objects.bulk_create(order_items)
        outter_items_to_create = [RequestItem(name=item['name'], description_quanity=item['quantityDescription'], description=item['description']) for item in outter_items]
        RequestItem.objects.bulk_create(outter_items_to_create)
        order.items.add(*order_items) 
        manager = TicketManager(order, email, name, phone, outter_items, address)
        if phone == '5546476943':
            whatsappManager = WhatsappManager(order, name, phone)
            whatsappManager.send_whatsapp()
        manager.create_excel()
        manager.send_ticket()
        return Response(OrderSerializer(order).data)
        