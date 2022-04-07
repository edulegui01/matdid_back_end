from django.db import models
from django.db.models import fields
from rest_framework import serializers
from apps.clientes.models import Cliente


class ClienteVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombre']