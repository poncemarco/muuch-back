from django.contrib import admin
from .models import Item, ItemOrder, RequestItem
from django.utils.html import format_html
from files.admin import ImageAdmin
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']  # Replace 'field1', 'field2', ... with the actual field names
    inlines = [ImageAdmin]

admin.site.register(Item, ItemAdmin)

admin.site.register(ItemOrder)
admin.site.register(RequestItem)