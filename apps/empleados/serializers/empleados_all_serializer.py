from django.db import models
from rest_framework import serializers
from apps.empleados.models import Empleado


class EmpleadoAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'