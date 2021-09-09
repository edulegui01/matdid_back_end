from rest_framework import viewsets
from apps.proveedores.serializers.proveedores_serializer_compra import ProveedorCompraSerializer


class ProveedoresCompraViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorCompraSerializer
    queryset = serializer_class.Meta.model.objects.all()
    pagination_class = None