from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from items.models import ItemOrder, Item    
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from django.shortcuts import get_object_or_404
from files.models import Ticket
from .functions import TicketManager

class OrderViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('items')
        order_items = []
        print(items)
        order = Order.objects.create()

        for item_data in items:
            item = get_object_or_404(Item, id=item_data['id'])
            order_items.append(ItemOrder(item=item, quantity=item_data['quantity']))

        ItemOrder.objects.bulk_create(order_items)
        order.items.add(*order_items) 
        manager = TicketManager(order)
        pdf_created = manager.create_pdf()
        print(pdf_created)
        manager.send_ticket()
        ticket = Ticket.objects.create(order=order, pdf_file=manager.ticket_path)
        order.ticket.set([ticket])
        
        return Response(OrderSerializer(order).data)
        