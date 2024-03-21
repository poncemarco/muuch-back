from django.contrib import admin
from files.models import Image

class ImageAdmin(admin.ModelAdmin):
    model = Image
    search_fields = ['item__name']  # Replace 'field1', 'field2', ... with the actual field names
    
admin.site.register(Image, ImageAdmin)


