from rest_framework import viewsets
from rest_framework.response import Response
from .models import Zone, Neighborhood
from .serializers import ZoneSerializer
from rest_framework.decorators import action
from .functions import check_postal_code

# Create your views here.
class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    
    @action(detail=False, methods=['get'], url_path='get-postal-address')
    def get_postal_address(self, request):
        postal_code = request.query_params.get('postal_code')
        if Zone.objects.filter(postal_code=postal_code).exists():
            zone = Zone.objects.get(postal_code=postal_code)
            return Response(ZoneSerializer(zone).data)
        address_response = check_postal_code(postal_code)
        if address_response["message"] == "Procesamiento correcto.": 
            new_postasl_code = Zone.objects.create(
                postal_code=postal_code, 
                state=address_response["codigo_postal"]["estado"], 
                county=address_response['codigo_postal']["municipio"]
            )
            for neighborhood in address_response['codigo_postal']["colonias"]:
                Neighborhood.objects.create(name=neighborhood, zone=new_postasl_code)
            return Response(ZoneSerializer(new_postasl_code).data)
        
        raise Exception("Error in the request")
        
    