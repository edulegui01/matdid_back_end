from calendar import month
from rest_framework import serializers


class VentaGraficaSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    total_vendido = serializers.IntegerField()




    def to_representation(self, instance):
       
       print(instance)
       return {
            'month': instance['month'],
            'total_vendido': instance['total_vendido']
       }    