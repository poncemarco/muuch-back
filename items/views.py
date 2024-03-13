from rest_framework import viewsets
from .models import Item, RequestItem, Category
from .serializers import ItemSerializer, RequestItemSerializer, CategorySerializer
from .paginators import ItemPaginator

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPaginator
    
    def get_queryset(self):
        queryset = Item.objects.filter(images__isnull=False)
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category).order_by('name')
            return queryset
        return queryset.order_by('name')
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class RequestItemViewSet(viewsets.ModelViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer
    