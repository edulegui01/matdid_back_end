from msilib.schema import Class
from rest_framework import serializers
from apps.compras.models import DetalleCompra


class DetalleCompraToEditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_producto = serializers.IntegerField()
    cantidad = serializers.IntegerField()
    precio = serializers.IntegerField()
    descuento = serializers.DecimalField(max_digits=5, decimal_places=2)
    precio_calculado = serializers.IntegerField()