from django.contrib import admin
from .models import Item, ItemOrder, RequestItem, Category
from django.utils.html import format_html
from files.admin import ImageAdmin
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']  
    inlines = [ImageAdmin]

admin.site.register(Item, ItemAdmin)

admin.site.register(ItemOrder)
admin.site.register(RequestItem)
admin.site.register(Category)