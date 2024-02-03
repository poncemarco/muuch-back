from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json

@csrf_exempt
@permission_classes([AllowAny])
def test_view(request):
    if request.method == 'POST':
        data  = request.body
        data = json.loads(data)
        print(data)  # Print incoming POST data
        return HttpResponse('Ok', status=200)
    if request.method == 'OPTIONS':
        return HttpResponse('OPTIONS', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)
    
    
