from rest_framework import viewsets,status
from rest_framework.response import Response
from apps.clientes.serializers.cobros_serializers import CobroSerializer
from apps.clientes.models import Cobro




class CobrosViewSet(viewsets.ModelViewSet):
    serializer_class = CobroSerializer
    queryset = Cobro.objects.values('id','id_cliente__nombre','id_cliente__sector',
        'id_cliente__localidad','id_cliente__nombre_encargado','fecha','monto').filter(state = True).order_by('id')

