from rest_framework import viewsets
from rest_framework.response import Response
from .models import Zones, Neighborhood
from .serializers import ZonesSerializer
from rest_framework.decorators import action
from .functions import check_postal_code

# Create your views here.
class ZonesViewSet(viewsets.ModelViewSet):
    queryset = Zones.objects.all()
    serializer_class = ZonesSerializer
    
    @action(detail=False, methods=['get'], url_path='get-postal-address')
    def get_postal_address(self, request):
        postal_code = request.query_params.get('postal_code')
        if Zones.objects.filter(postal_code=postal_code).exists():
            zone = Zones.objects.get(postal_code=postal_code)
            return Response(ZonesSerializer(zone).data)
        address_response = check_postal_code(postal_code)
        if address_response["message"] == "Procesamiento correcto.":
            new_postasl_code = Zones.objects.create(
                postal_code=postal_code, 
                state=address_response["codigo_postal"]["estado"], 
                county=address_response['codigo_postal']["municipio"]
            )
            for neighborhood in address_response['codigo_postal']["colonias"]:
                new_neighborhood = Neighborhood.objects.create(name=neighborhood, zone=new_postasl_code)
            zone = Zones.objects.get(postal_code=postal_code)
            return Response(ZonesSerializer(zone).data)
        
        raise Exception("Error in the request")
        
    