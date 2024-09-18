from django.db import models

class Neighborhood(models.Model):
    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'
        
    name = models.CharField(max_length=50)
    zone = models.ForeignKey('Zone', on_delete=models.CASCADE, related_name='neighborhoods')
    
    def __str__(self):
        return self.name
    
class Zone(models.Model):
    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
    postal_code = models.CharField(max_length=5)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    #neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='zones')
    
    def __str__(self):
        return self.postal_code
    
    
