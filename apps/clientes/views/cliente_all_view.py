from ast import Return
from rest_framework import viewsets,status

from apps.clientes.serializers.cliente_all_serializer import ClienteAllSerializer
from apps.clientes.models import Cliente


class EmpleadoAllView(viewsets.ModelViewSet):
    serializer_class = ClienteAllSerializer
    queryset = Cliente.objects.filter(state = True)