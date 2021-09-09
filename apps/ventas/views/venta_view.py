from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.ventas.serializers.ventas_serializer import VentaSerializer
from apps.ventas.serializers.create_venta_serializer import CreateVentaSerializer
from apps.ventas.serializers.detalle_venta_serializer import DetalleVentaSerializer
from apps.ventas.models import Venta
from apps.base.funcionalidades_bases import carga_detalle_compra, cargar_datos


class VentasViewsSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset =  Venta.objects.values('id','id_cliente__nombre','id_cliente__sector',
            'id_cliente__localidad','id_empleado__nombre','accion','Fecha','monto_total').filter(state=True).order_by('id')

    """def get_queryset(self,pk=None):
        if pk:
            return Venta.objects.values('id','id_cliente__nombre','id_cliente__sector',
            'id_cliente__localidad','id_empleado__nombre','accion','Fecha','monto_total').filter(state=True,id=pk).first()
        return Venta.objects.values('id','id_cliente__nombre','id_cliente__sector',
            'id_cliente__localidad','id_empleado__nombre','accion','Fecha','monto_total').filter(state=True).order_by('id')

    def list(self,request):
        return Response(self.serializer_class(self.get_queryset(), many=True).data,status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk = None):
        if self.get_queryset(pk):
            return Response(self.serializer_class(self.get_queryset(pk)).data)
        return Response({'mensaje':'venta no encontrada'}, status = status.HTTP_404_NOT_FOUND)"""

    def create(self, request):
        venta_claves = ['accion','id_cliente','id_empleado','monto_total','detalle_venta']
        venta_valores = list(map(request.data.get,venta_claves))

        venta = cargar_datos(venta_claves,venta_valores)
        
        
        compra_serializer = CreateVentaSerializer(data =venta)
        if compra_serializer.is_valid():
            compra_serializer.save()
        else:
            return Response(compra_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        detalle_venta = carga_detalle_compra(venta_claves,venta_valores,Venta,"detalle_venta","id_venta")

        detalle_venta_serializer = DetalleVentaSerializer(data=detalle_venta, many=True)
        
        if detalle_venta_serializer.is_valid():    
            detalle_venta_serializer.save()
            return Response(compra_serializer.data, status = status.HTTP_200_OK)
        return Response({'mesagge':'no se pudo crear el detalle venta'}, status = status.HTTP_400_BAD_REQUEST) 
        

    def update(self, request, pk=None):
        queryset = Venta.objects.all().filter(id=pk).first()
        venta_serializer = CreateVentaSerializer(queryset,data = request.data)
        if venta_serializer.is_valid():
            venta_serializer.save()
            return Response(venta_serializer.data, status = status.HTTP_200_OK)
        return Response(venta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request, pk=None):
        venta = Venta.objects.filter(state = True,id=pk).first()

        if venta:
            venta.state=False
            venta.save()
            return Response({'mensaje': 'venta eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'mensaje': 'No existe esa venta'}, status = status.HTTP_400_BAD_REQUEST)