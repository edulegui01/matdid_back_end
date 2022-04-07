from django.db import models
from rest_framework import serializers
from apps.productos.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'autor': instance.autor,
            'costo': instance.costo,
            'precio': instance.precio,
            'stock': instance.stock_actual,
            'fecha': instance.create_date
        }