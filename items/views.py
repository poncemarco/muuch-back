from .models import Item, RequestItem, Category
from .serializers import ItemSerializer, RequestItemSerializer, CategorySerializer
from .paginators import ItemPaginator
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.db.models import Count

class ItemViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = ItemPaginator
    
    def get_queryset(self):
        queryset = Item.objects.filter(images__isnull=False)
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category)
            return queryset
        return queryset.order_by('name')
    
    
class CategoryViewSet(ListModelMixin, GenericViewSet):
    model = Category
    queryset = Category.objects.prefetch_related('items').all().annotate(
        number_of_items= Count('items')
    ).order_by('number_of_items')
    serializer_class = CategorySerializer
    
    
class RequestItemViewSet(ListModelMixin, GenericViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer
    