from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Image

def get_image_thumbnail(request, image_id):
    image = Image.objects.get(pk=image_id)
    thumbnail_url = image.thumbnail.url  # Esto proporcionará la URL de la miniatura generada
    return JsonResponse({'thumbnail_url': thumbnail_url})