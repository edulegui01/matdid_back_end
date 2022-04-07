from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.compras.serializers.compras_all_serializer import ComprasAllSerializer
from apps.compras.models import Compra, DetalleCompra
from apps.compras.serializers.create_compra_serializer import CreateCompraSerializer
from apps.base.funcionalidades_bases import carga_detalle_compra, cargar_datos
from apps.compras.serializers.detalle_compra_serializer import DetalleCompraSerializer




class CompraUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = ComprasAllSerializer
    queryset = Compra.objects.all()



    def update(self, request, pk=None):
        queryset = Compra.objects.filter(id=pk).first()
        detalle_compra_delete = DetalleCompra.objects.filter(id_compra = pk)
        compra_claves = ['accion','id_proveedor','id_empleado','monto_total','detalles']
        compra_valores = list(map(request.data.get,compra_claves))
        compra = cargar_datos(compra_claves,compra_valores)
        
        
        compra_serializer = CreateCompraSerializer(queryset,data = compra)
        
        if compra_serializer.is_valid():
            compra_serializer.save()
            detalle_compra = carga_detalle_compra(compra_claves,compra_valores,Compra,"detalles","id_compra",pk)
            print(carga_detalle_compra)
            for detalle_only_query in detalle_compra_delete:
                query_detalle = DetalleCompra.objects.filter(id=detalle_only_query.id).first()
                query_detalle.delete()
            
            
            detalle_compra_serializer = DetalleCompraSerializer(data=detalle_compra, many=True)
            if detalle_compra_serializer.is_valid():
                detalle_compra_serializer.save()
                return Response({'message':'La compra se acutalizó correctamente'}, status = status.HTTP_200_OK)
            else:
                return Response({'error':'Los datos no son validos'}, status = status.HTTP_400_BAD_REQUEST)
            