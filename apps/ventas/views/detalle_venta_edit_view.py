from rest_framework import viewsets, status
from apps.ventas.serializers.detalle_venta_edit_serializer import DetalleVentaEditSerializer
from apps.ventas.models import DetalleVenta
from rest_framework.response import Response


class DetalleCompraEditView(viewsets.ModelViewSet): 
    queryset=DetalleVenta.objects.values('id_producto','cantidad','precio','descuento','precio_calculado').filter(state = True)
    serializer_class = DetalleVentaEditSerializer

    def retrieve(self,request,pk):
        print(pk)
        query_set = DetalleVenta.objects.values('id_producto','cantidad','precio','descuento','precio_calculado').filter(state = True,id_venta=pk)
        
        detalle_compra_edit_serializer = DetalleVentaEditSerializer(query_set,many=True) 
        print(detalle_compra_edit_serializer.data)
        return Response(detalle_compra_edit_serializer.data,status = status.HTTP_200_OK)