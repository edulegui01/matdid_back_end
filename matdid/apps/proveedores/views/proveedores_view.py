from rest_framework import viewsets
from apps.proveedores.serializers.proveedores_serializers import ProveedorSerializer
from apps.proveedores.models import Pago


class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Pago.objects.values('id','id_proveedor__nombre','id_proveedor__localidad','id_proveedor__nombre_encargado','fecha','monto')