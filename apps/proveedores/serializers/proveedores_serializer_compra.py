from rest_framework import serializers
from apps.proveedores.models import Proveedor


class ProveedorCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id','nombre')