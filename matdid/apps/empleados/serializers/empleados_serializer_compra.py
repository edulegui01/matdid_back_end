from rest_framework import serializers
from apps.empleados.models import Empleado


class EmpleadoCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id','nombre')