from rest_framework import serializers

from .models import Zones, Neighborhood


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['name']



class ZonesSerializer(serializers.ModelSerializer):
    neighborhoods = serializers.SerializerMethodField()
    
    def get_neighborhoods(self, obj):
        return NeighborhoodSerializer(obj.neighborhoods.all(), many=True).data
    class Meta:
        model = Zones
        fields = ['id', 'postal_code', 'state', 'county', 'neighborhoods']
        
        