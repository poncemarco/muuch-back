from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario')
    items = models.ManyToManyField('items.ItemOrder', verbose_name='Productos')
    payment = models.ForeignKey('payments.Payment', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pago')
    discount = models.ForeignKey('DiscountCode', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cupon')
    
    def get_total(self):
        if self.discount and self.discount.active:
            discount_factor = Decimal(str(self.discount.discount_factor))  # Convertir a Decimal
            return round(sum([item.get_total_item_price() * float(discount_factor) for item in self.items.all()]), 2)
        return round(sum([item.get_total_item_price() for item in self.items.all()]), 2)
    
    get_total.short_description = 'Total de la Orden'
    
    def get_total_items(self):
        return int(sum([item.quantity for item in self.items.all()]))
    
    get_total_items.short_description = 'Cantidad de Productos'
    
    def get_discount(self):
        if self.discount and self.discount.active:
            discount_factor = Decimal(str(self.discount.discount_factor))  # Convertir a Decimal
            return round(sum([item.get_total_item_price() * (1 - float(discount_factor)) for item in self.items.all()]), 2)
        
    get_discount.short_description = 'Descuento Aplicado'
    
    class Meta:
        verbose_name_plural = 'Ordenes'
        verbose_name = 'Orden'

class DiscountCode(models.Model):
    code = models.CharField(max_length=15)
    discount_factor = models.FloatField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name_plural = 'Cupones'
        verbose_name = 'Cupon'
        
    