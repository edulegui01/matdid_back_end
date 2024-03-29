from django.db import models
from rest_framework import serializers
from apps.proveedores.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'ruc': instance.ruc,
            'razon_social': instance.razon_social,
            'localidad': instance.localidad,
            'total_cobrado': instance.total_cobrado,
            'deuda_por_cobrar': instance.deuda_por_cobrar
        }
    