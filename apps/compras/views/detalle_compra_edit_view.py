from rest_framework import viewsets, status
from apps.compras.serializers.detalle_compra_edit_serializer import DetalleCompraToEditSerializer
from apps.compras.models import DetalleCompra
from rest_framework.response import Response


class DetalleCompraEditView(viewsets.ModelViewSet): 
    queryset=DetalleCompra.objects.values('id_producto','cantidad','precio','descuento','precio_calculado').filter(state = True)
    serializer_class = DetalleCompraToEditSerializer

    def retrieve(self,request,pk):
        print(pk)
        query_set = DetalleCompra.objects.values('id','id_producto','cantidad','precio','descuento','precio_calculado').filter(state = True,id_compra=pk)
        
        detalle_compra_edit_serializer = DetalleCompraToEditSerializer(query_set,many=True) 
        print(detalle_compra_edit_serializer.data)
        return Response(detalle_compra_edit_serializer.data,status = status.HTTP_200_OK)
