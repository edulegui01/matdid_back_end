from cgi import print_directory
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.ventas.serializers.ventas_serializer import VentaSerializer
from apps.ventas.serializers.create_venta_serializer import CreateVentaSerializer
from apps.ventas.serializers.detalle_venta_serializer import DetalleVentaSerializer
from apps.ventas.models import DetalleVenta, Venta
from apps.base.funcionalidades_bases import carga_detalle_compra, cargar_datos
from apps.productos.models import Producto


class VentasViewsSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset =  Venta.objects.values('id','id_cliente__nombre','id_cliente__sector',
            'id_cliente__localidad','id_empleado__nombre','accion','Fecha','monto_total').filter(state=True).order_by('id')


    def create(self, request):
        venta_claves = ['accion','id_cliente','id_empleado','monto_total','detalles']
        venta_valores = list(map(request.data.get,venta_claves))
        detalle_venta = carga_detalle_compra(venta_claves,venta_valores,Venta,"detalles","id_venta")
        messages_alert=[]
        venta = cargar_datos(venta_claves,venta_valores)

        if len(venta['detalles']) == 0 or venta['id_cliente'] == "" or venta['id_empleado'] == "":
            return Response({'message':'Por favor, complete los datos necesarios para realizar la compra'},status = status.HTTP_400_BAD_REQUEST)
        else:
            for detalle_producto in detalle_venta:
                query_producto = Producto.objects.filter(state = True, id = detalle_producto['id_producto']).first()
                print(query_producto)
                resto_stock_producto = query_producto.stock_actual-detalle_producto['cantidad']
                if resto_stock_producto < 0:
                    return Response({'message':f'No se puede realizar la compra, quedan {query_producto.stock_actual} unidades de {query_producto.nombre}'}, status = status.HTTP_400_BAD_REQUEST)
                elif resto_stock_producto <= query_producto.stock_minimo:
                    messages_alert.append(f'Quedan {resto_stock_producto} unidades del producto {query_producto.nombre}. Es necesario la compra de más unidades')            
                query_producto.stock_actual = resto_stock_producto
                query_producto.save()
        
        venta_serializer = CreateVentaSerializer(data =venta)
        if venta_serializer.is_valid():
            venta_serializer.save()
        else:
            return Response(venta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        detalle_venta = carga_detalle_compra(venta_claves,venta_valores,Venta,"detalles","id_venta")

        detalle_venta_serializer = DetalleVentaSerializer(data=detalle_venta, many=True)
        
        if detalle_venta_serializer.is_valid():    
            detalle_venta_serializer.save()
            return Response({'message':'Se ha creado la venta con éxito','message_alert':messages_alert}, status = status.HTTP_200_OK)
        return Response(detalle_venta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

    def update(self, request, pk=None):
        queryset = Venta.objects.all().filter(id=pk).first()
        venta_serializer = CreateVentaSerializer(queryset,data = request.data)
        if venta_serializer.is_valid():
            venta_serializer.save()
            return Response(venta_serializer.data, status = status.HTTP_200_OK)
        return Response(venta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request, pk=None):
        venta_query = Venta.objects.filter(state = True,id=pk).first()
        detalle_venta_query = DetalleVenta.objects.filter(state = True, id_venta=pk)
        print(venta_query)
        
        if venta_query and detalle_venta_query:
            venta_query.state=False
            venta_query.save()
            for detalle_only_query in detalle_venta_query:
                query_detalle = DetalleVenta.objects.filter(id=detalle_only_query.id).first()
                query_detalle.state = False
                query_detalle.save()
            return Response({'mensaje': 'Venta eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'mensaje': 'No existe esa venta'}, status = status.HTTP_400_BAD_REQUEST)