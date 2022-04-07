from django.db import models
from rest_framework import serializers
from apps.productos.models import Producto


class ProductoAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'