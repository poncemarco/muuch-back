from django.contrib import admin
from .models import Item, ItemOrder, RequestItem, Category
from django.utils.safestring import mark_safe
from files.admin import ImageAdmin
from django.db import models
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']  
    empty_value_display = "-"
    fields = ["name", "unit", "price", "category", "apply_tax_iva", "image_tag"]
    list_display = ["name", "price", "category", "unit", "price_display_admin"]
    readonly_fields = ["image_tag"]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']  
    empty_value_display = "-"
    fields = ["name"]
    list_display = ["name"]
    
        

admin.site.register(Item, ItemAdmin)
admin.site.register(RequestItem)


admin.site.register(Category, CategoryAdmin)