from rest_framework import serializers
from apps.compras.models import Compra

class CreateCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields =['accion','id_empleado','id_proveedor','monto_total']


    def update(self, instance,validated_data):
        #print(instance.accion)
        instance.accion = validated_data.get('accion',instance.accion)
        instance.id_empleado = validated_data.get('id_empleado',instance.id_empleado)
        instance.id_proveedor = validated_data.get('id_proveedor',instance.id_proveedor)
        instance.monto_total= validated_data.get('monto_total',instance.monto_total)
        instance.save()
        return instance