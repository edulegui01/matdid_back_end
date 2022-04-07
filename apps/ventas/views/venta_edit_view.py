from rest_framework import viewsets
from apps.ventas.serializers.ventas_edit_serializer import VentasEditSerializer
from apps.ventas.models import Venta


class VentasEditViewset(viewsets.ModelViewSet):
    serializer_class = VentasEditSerializer
    queryset = Venta.objects.values('id','accion','id_cliente','id_empleado','monto_total').filter(state = True).order_by('id')