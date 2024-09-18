from django.contrib import admin
from .models import Zone

# Register your models here.
class ZonesAdmin(admin.ModelAdmin):
    list_display = ('postal_code', 'state', 'county')
    search_fields = ('postal_code', 'state', 'county')
    list_filter = ('state', 'county')
    
    
admin.site.register(Zone, ZonesAdmin)