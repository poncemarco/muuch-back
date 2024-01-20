from django.contrib import admin
from .models import Item, ItemOrder, RequestItem
# Register your models here.

admin.site.register(Item)
admin.site.register(ItemOrder)
admin.site.register(RequestItem)