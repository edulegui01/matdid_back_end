from django.db import models
from rest_framework import serializers
from apps.clientes.models import Cliente


class ClienteAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'