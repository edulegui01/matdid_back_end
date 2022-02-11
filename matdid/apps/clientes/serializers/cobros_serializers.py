from rest_framework import serializers


class CobroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_cliente__nombre = serializers.CharField(max_length=225)
    id_cliente__sector = serializers.CharField(max_length=225)
    id_cliente__localidad = serializers.CharField(max_length=225)
    id_cliente__nombre_encargado = serializers.CharField(max_length=225)
    fecha = serializers.DateField()
    monto= serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'cliente': instance['id_cliente__nombre'],
            'ciudad': instance['id_cliente__localidad'],
            'encargado': instance['id_cliente__nombre_encargado'],
            'sector': instance['id_cliente__sector'],
            'fecha': instance['fecha'],
            'monto': instance['monto']
        }
