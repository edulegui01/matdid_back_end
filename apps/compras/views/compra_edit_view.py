from rest_framework import viewsets
from apps.compras.serializers.compras_edit_serializer import ComprasEditSerializer
from apps.compras.models import Compra


class ComprasEditViewset(viewsets.ModelViewSet):
    serializer_class = ComprasEditSerializer
    queryset = Compra.objects.values('id','accion','id_proveedor','id_empleado','monto_total').filter(state = True).order_by('id')