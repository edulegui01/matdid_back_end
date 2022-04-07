from rest_framework import serializers

class VentasEditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    accion = serializers.CharField(max_length=225)
    id_cliente = serializers.IntegerField()
    id_empleado = serializers.IntegerField()
    monto_total = serializers.IntegerField()