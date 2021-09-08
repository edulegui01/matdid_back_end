from rest_framework import serializers
from apps.proveedores.models import Proveedor



class ProveedorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_proveedor__nombre = serializers.CharField(max_length=225)
    id_proveedor__localidad = serializers.CharField(max_length=225)
    id_proveedor__nombre_encargado = serializers.CharField(max_length=225)
    fecha = serializers.DateField()
    monto = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'proveedor': instance['id_proveedor__nombre'],
            'ciudad': instance['id_proveedor__localidad'],
            'encargado': instance['id_proveedor__nombre_encargado'],
            'fecha': instance['fecha'],
            'monto': instance['monto']
        }
    