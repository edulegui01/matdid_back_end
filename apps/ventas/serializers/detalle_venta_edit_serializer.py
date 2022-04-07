from rest_framework import serializers


class DetalleVentaEditSerializer(serializers.Serializer):
    id_producto = serializers.IntegerField()
    cantidad = serializers.IntegerField()
    precio = serializers.IntegerField()
    descuento = serializers.DecimalField(max_digits=5, decimal_places=2)
    precio_calculado = serializers.IntegerField()