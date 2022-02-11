from rest_framework import viewsets
from apps.clientes.serializers.clientes_ventas_serializer import ClienteVentaSerializer


class ClientesVentaViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteVentaSerializer
    queryset = serializer_class.Meta.model.objects.all()
    pagination_class = None