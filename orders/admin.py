from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Order, DiscountCode

# Admin para el modelo Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    name = 'Ordenes'  # Nombre de la sección en el admin
    list_display = ('id', 'user', 'get_total_items', 'get_total', 'payment', 'discount')  # Campos a mostrar en la lista
    search_fields = ('user__username', 'discount__code')  # Campos por los que se puede buscar
    list_filter = ('user', 'payment', 'discount')  # Filtros laterales
    readonly_fields = ('get_total', 'get_total_items', 'get_discount')  # Campos de solo lectura en el formulario
    filter_horizontal = ('items',)  # Para que el campo ManyToMany se vea mejor en el admin
    
    fieldsets = (
        (None, {
            'fields': ('user', 'items', 'payment', 'discount')
        }),
        ('Información del Total', {
            'fields': ('get_total', 'get_total_items', 'get_discount'),
        }),
    )
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related('items') # Prefetch para evitar N+1 queries

# Admin para el modelo DiscountCode
@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_factor', 'active')  # Campos a mostrar en la lista
    search_fields = ('code',)  # Campo por el que se puede buscar
    list_filter = ('active',)  # Filtro para el campo activo
