from django.db import models
from rest_framework import serializers
from apps.clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'ruc': instance.ruc,
            'razon_social': instance.razon_social,
            'localidad': instance.localidad,
            'total_comprado': instance.total_comprado,
            'deuda_por_pagar': instance.deuda_por_pagar
        }