from calendar import month
from os import stat
from apps.ventas.models import DetalleVenta
from django.db.models import Count, Sum
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models.functions import TruncMonth
from apps.ventas.serializers.venta_grafica_serializer import VentaGraficaSerializer



class VentasGraficaViewset(viewsets.ViewSet):
    
    
    def list(self, request):
        queryset = DetalleVenta.objects.values().annotate(month = TruncMonth('create_date')).values('month').annotate(total_vendido= Sum('cantidad')).values('month','total_vendido').order_by('month')
        print(queryset)

        for query_month in queryset:
            query_month['month'] = query_month['month'].month
        
        venta_grafica_serializer = VentaGraficaSerializer(queryset,many=True)

        return Response(venta_grafica_serializer.data, status = status.HTTP_200_OK)