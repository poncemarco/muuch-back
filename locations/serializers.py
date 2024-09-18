from rest_framework import serializers

from .models import Zone, Neighborhood


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['name']



class ZoneSerializer(serializers.ModelSerializer):
    neighborhoods = serializers.SerializerMethodField()
    
    def get_neighborhoods(self, obj):
        return NeighborhoodSerializer(obj.neighborhoods.all(), many=True).data
    class Meta:
        model = Zone
        fields = ['id', 'postal_code', 'state', 'county', 'neighborhoods']
        
        