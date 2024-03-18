from rest_framework import serializers

from .models import Zones, Neighborhood

class NeighborhoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ["name"]

class ZonesSerializer(serializers.ModelSerializer):
    neighborhoods = NeighborhoodsSerializer(many=True, read_only=True)
    class Meta:
        model = Zones
        fields = ['id', 'postal_code', 'state', 'county', 'neighborhoods']
        
        