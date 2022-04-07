from rest_framework import serializers
from apps.empleados.models import Empleado

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre+" "+instance.apellido,
            'cedula': instance.cedula,
            'telefono': instance.telefono,
            'domicilio': instance.domicilio,
            'localidad': instance.localidad,
            'email': instance.email,
            'rol': instance.rol
        }
