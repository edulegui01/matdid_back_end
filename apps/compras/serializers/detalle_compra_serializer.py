from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.compras.models import DetalleCompra

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = '__all__'