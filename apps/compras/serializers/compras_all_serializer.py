from rest_framework import serializers
from apps.compras.models import Compra


class ComprasAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields ='__all__'