from django.contrib import admin
from .models import Order
from django.contrib import admin
from .models import Order
from files.models import Ticket
# Register your models here.


class TicketInline(admin.TabularInline):
    model = Ticket

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [TicketInline]



