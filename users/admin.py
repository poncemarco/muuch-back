from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Phone, Address

# Define your custom UserAdmin class here

class PhoneInline(admin.StackedInline):
    model = Phone
    can_delete = False
    verbose_name_plural = 'Telefonos'
    verbose_name = 'Telefono'
    
class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name_plural = 'Direcciones'
    verbose_name = 'Direccion'

class CustomUserAdmin(BaseUserAdmin):
    inlines = [PhoneInline, AddressInline]
    

# Unregister the default User admin
admin.site.unregister(User)

# Register User with your custom UserAdmin
admin.site.register(User, CustomUserAdmin)
