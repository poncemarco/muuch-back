from django.db import models
from django_extensions.db.models import TimeStampedModel
from uuid import uuid4 as uuid

# Create your models here.
class Payment(TimeStampedModel):
    public_id = models.UUIDField(primary_key=True, editable=False, default=uuid, unique=True, verbose_name='ID Público')
    status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Pagos'
        verbose_name = 'Pago'