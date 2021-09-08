from rest_framework import serializers
from apps.compras.models import Compra

class CreateCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields =['accion','id_empleado','id_proveedor','monto_total']


