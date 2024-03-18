from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    zone = models.ForeignKey('Zones', on_delete=models.CASCADE, related_name='neighborhoods')
    
    def __str__(self):
        return self.name
    
class Zones(models.Model):
    postal_code = models.CharField(max_length=5)
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='zones')
    
    def __str__(self):
        return self.postal_code
    
    
