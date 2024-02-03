from django.db import models
from versatileimagefield.fields import VersatileImageField
from orders.models import Order

class Image(models.Model):
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name='images')
    image_path = VersatileImageField(
        'Image',
        upload_to='images/products_images/',
        width_field='width',
        height_field='height'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self):
        return self.item.name + " - " + str(self.id)
    
    

class Ticket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='ticket')
    pdf_file = models.FileField(upload_to='ticket_pdfs/')
