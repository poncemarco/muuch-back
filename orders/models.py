from django.db import models
from decimal import Decimal

# Create your models here.
class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('items.ItemOrder')
    payment = models.ForeignKey('payments.Payment', on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.ForeignKey('DiscountCode', on_delete=models.SET_NULL, null=True, blank=True)
    
    def get_total(self):
        if self.discount and self.discount.active:
            discount_factor = Decimal(str(self.discount.discount_factor))  # Convertir a Decimal
            return sum([item.get_total_item_price() * float(discount_factor) for item in self.items.all()])
        return sum([item.get_total_item_price() for item in self.items.all()])
    
    def get_discount(self):
        if self.discount and self.discount.active:
            discount_factor = Decimal(str(self.discount.discount_factor))  # Convertir a Decimal
            return sum([item.get_total_item_price() * (1 - float(discount_factor)) for item in self.items.all()])
    
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
        
    