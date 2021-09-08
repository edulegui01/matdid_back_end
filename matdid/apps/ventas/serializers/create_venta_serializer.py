from rest_framework import serializers
from apps.ventas.models import Venta

class CreateVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['accion','id_cliente','id_empleado','monto_total']