from django.db import models
from uuid import uuid4 as uuid

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid, unique=True, verbose_name='ID Público')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    
    def price_display(self):
        return float(self.price) * 1.2
    
    def main_image(self):
        return self.images.first()
        
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        
    
    def __str__(self):
        return self.name
    
class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    
    def get_total_item_price(self):
        return self.quantity * self.item.price_display()
    
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
class RequestItem(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    description_quanity = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Productos Solicitados'
        verbose_name = 'Producto Solicitado'
        
class RequestItemOrder(models.Model):
    items = models.ForeignKey(RequestItem, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'
        
    def __str__(self):
        return self.name
