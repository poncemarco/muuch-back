from django.contrib import admin
from .models import Order
from django.contrib import admin
from .models import Order, DiscountCode
from files.models import Ticket
# Register your models here.


class TicketInline(admin.TabularInline):
    model = Ticket

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [TicketInline]
    
@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    model = DiscountCode
    


