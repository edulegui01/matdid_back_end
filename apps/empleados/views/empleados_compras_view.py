from rest_framework import viewsets
from apps.empleados.serializers.empleados_serializer_compra import EmpleadoCompraSerializer


class EmpleadosCompraViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoCompraSerializer
    queryset = serializer_class.Meta.model.objects.all().filter(state = True)
    pagination_class = None