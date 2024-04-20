from django.contrib import admin
from django.contrib import admin
from .models import Order, DiscountCode

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    search_fields = ['payment__payment_id']
    empty_value_display = "-"
    list_display = ["get_total", "get_total_items", "get_discount", "discount"]
    readonly_fields = ["get_total", "get_total_items", "get_discount"]

    
admin.site.register(Order, OrderAdmin)
    


