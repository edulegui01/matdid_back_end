from rest_framework import serializers

class VentaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_cliente__nombre = serializers.CharField(max_length=225)
    id_cliente__sector = serializers.CharField(max_length=255)
    id_cliente__localidad = serializers.CharField(max_length=225)
    id_empleado__nombre = serializers.CharField(max_length=225)
    accion = serializers.CharField(max_length=225)
    Fecha = serializers.DateField()
    monto_total = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'cliente': instance['id_cliente__nombre'],
            'sector':instance['id_cliente__sector'],
            'ciudad': instance['id_cliente__localidad'],
            'encargado': instance['id_empleado__nombre'],
            'accion': instance['accion'],
            'fecha': instance['Fecha'],
            'monto_total': instance['monto_total']
        }