from rest_framework import serializers


class ComprasEditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    accion = serializers.CharField(max_length=225)
    id_proveedor = serializers.IntegerField()
    id_empleado = serializers.IntegerField()
    monto_total = serializers.IntegerField()
