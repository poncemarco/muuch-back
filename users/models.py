from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from locations.models import Zones

# Create your models here.
class Phone(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name_plural = 'Telefonos'
        verbose_name = 'Telefono'
        
        
class Address(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    particular_reference = models.CharField(max_length=254, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Direcciones'
        verbose_name = 'Direccion'