from rest_framework import serializers
from .models import Address
from django.contrib.auth.models import User
from rest_framework import serializers
from phone_field import PhoneField

ERROR_PHONE_MESSAGES = {
    'required': 'El telefono es requerido',
    'invalid': 'Ingrese un telefono valido',
}

class FormUserSerializer(serializers.ModelSerializer):
    phone = PhoneField(verbose_name='Telefono', help_text='Telefono', error_messages=ERROR_PHONE_MESSAGES)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'phone']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'