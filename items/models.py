from django.db import models
from uuid import uuid4 as uuid
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import admin

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid, unique=True, verbose_name='ID Público')
    name = models.CharField(max_length=100, verbose_name='Producto')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Precio')
    unit = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unidad')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoría')
    apply_tax_iva = models.BooleanField(default=False, verbose_name='Aplica IVA')
    
    
    @property
    @admin.display(
        description="Precio de venta"
    )
    def price_display_admin(self):
        if self.category == 'Cristaleria':
            result = round(float(self.price) * 1.2, 2)
            return '{:.2f}'.format(result)
        return '{:.2f}'.format(round(float(self.price) * 1.2, 2))
    
    def price_display(self):
        if self.category == 'Cristaleria':
            result = round(float(self.price) * 1.2, 2)
            return '{:.2f}'.format(result)
        return '{:.2f}'.format(round(float(self.price) * 1.2, 2))
    
    def main_image(self):
        return self.images.first()
    
    
    def slug(self):
        return self.name.lower().replace(' ', '-').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('/', ('_'))
        
    @admin.display(description="Imagen")
    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.main_image().link()))
     
    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        
    
    def __str__(self):
        return self.name
    
class ItemOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_total_item_price(self):
        return float(self.quantity) * self.item.price_display()
    
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
