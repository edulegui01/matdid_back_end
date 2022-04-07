from django.db import models
from rest_framework import serializers
from apps.proveedores.models import Proveedor


class ProveedorAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'