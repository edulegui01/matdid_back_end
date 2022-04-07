from rest_framework import serializers
from apps.productos.models import Producto


class ProductoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','costo')