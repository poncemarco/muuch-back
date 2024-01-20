from django.db import models

# Create your models here.
class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('items.ItemOrder')
    payment = models.ForeignKey('payments.Payment', on_delete=models.SET_NULL, null=True, blank=True)
    
    def get_total(self):
        return sum([item.get_total_item_price() for item in self.items.all()])
    
    class Meta:
        verbose_name_plural = 'Ordenes'
        verbose_name = 'Orden'
    