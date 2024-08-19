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
from locations.models import Zones, Neighborhood
from users.functions import set_name


class OrderViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('items')
        name = request.data.pop('name')
        email = request.data.pop('email')
        phone = request.data.pop('phone')
        outer_items = request.data.pop('outterItems')
        address = request.data.pop('address')
        user, is_new_user = User.objects.get_or_create(email=email, username=email)
        if is_new_user:
            first_name, last_name = set_name(name)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        Phone.objects.get_or_create(user=user, phone=phone)
        zone = Zones.objects.filter(postal_code=address["postalCode"]).first()
        neighborhood = Neighborhood.objects.filter(name=address['neighborhood']).first()
        if zone:
            Address.objects.get_or_create(user=user, street=address['street'],  zone=zone, particular_reference=address['complement'], neighborhood=neighborhood)
        discount = None
        if 'coupon' in request.data:
            try:
                discount = DiscountCode.objects.get(code=request.data['coupon'])
            except DiscountCode.DoesNotExist:
                pass
        order_items = []
        order = Order.objects.create(discount=discount, user=user)

        for item_data in items:
            item = get_object_or_404(Item, id=item_data['id'])
            order_items.append(ItemOrder(item=item, quantity=item_data['quantity']))

        ItemOrder.objects.bulk_create(order_items)
        outer_items_to_create = [RequestItem(name=item['name'], description_quanity=item['quantityDescription'], description=item['description']) for item in outer_items]
        RequestItem.objects.bulk_create(outer_items_to_create)
        order.items.add(*order_items) 
        # manager = TicketManager(order, email, name, phone, outer_items, address)
        # if phone == '5546476943':
        #     whatsappManager = WhatsappManager(order, name, phone)
        #     whatsappManager.send_whatsapp()
        # manager.create_excel()
        # manager.send_ticket()
        return Response(OrderSerializer(order).data)
        