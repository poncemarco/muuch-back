from rest_framework import viewsets
from .models import Item, RequestItem
from .serializers import ItemSerializer, RequestItemSerializer
from .paginators import ItemPaginator

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(images__isnull=False).distinct().order_by('?')
    serializer_class = ItemSerializer
    pagination_class= ItemPaginator
    
    
class RequestItemViewSet(viewsets.ModelViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer
    