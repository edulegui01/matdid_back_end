from django.db import models
from apps.compras.models import Compra
from rest_framework import serializers

class CompraSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_proveedor__nombre = serializers.CharField(max_length=225)
    id_proveedor__localidad = serializers.CharField(max_length=225)
    id_empleado__nombre = serializers.CharField(max_length=225)
    accion = serializers.CharField(max_length=225)
    Fecha = serializers.DateField()
    monto_total = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'proveedor': instance['id_proveedor__nombre'],
            'ciudad': instance['id_proveedor__localidad'],
            'encargado': instance['id_empleado__nombre'],
            'accion': instance['accion'],
            'fecha': instance['Fecha'],
            'monto_total': instance['monto_total']
        }
