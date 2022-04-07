from ast import Return
from rest_framework import viewsets,status

from apps.empleados.serializers.empleados_all_serializer import EmpleadoAllSerializer
from apps.empleados.models import Empleado


class EmpleadoAllView(viewsets.ModelViewSet):
    serializer_class = EmpleadoAllSerializer
    queryset = Empleado.objects.filter(state = True)