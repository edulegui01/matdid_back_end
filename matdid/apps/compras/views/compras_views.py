from django.db.models import query
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.compras.serializers.compras_serializer import CompraSerializer
from apps.compras.serializers.create_compra_serializer import CreateCompraSerializer
from apps.compras.serializers.detalle_compra_serializer import DetalleCompraSerializer
from apps.usuarios.authentication_mixin import Authentication
from apps.compras.models import Compra, DetalleCompra
from apps.base.funcionalidades_bases import carga_detalle_compra, cargar_datos


"""class LargeResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'"""


class ComprasViewSet(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.values('id','accion','id_proveedor__nombre',
        'id_proveedor__localidad','id_empleado__nombre','Fecha','monto_total').filter(state = True).order_by('id')
    
    """def get_queryset(self, pk=None):
        if pk:
            return Compra.objects.values('id','accion','id_proveedor__nombre',
            'id_proveedor__localidad','id_empleado__nombre','Fecha','monto_total').filter(state = True,id=pk).first()   
        
        return Compra.objects.values('id','accion','id_proveedor__nombre',
        'id_proveedor__localidad','id_empleado__nombre','Fecha','monto_total').filter(state = True).order_by('id')

        

    def list(self, request):
        return Response(self.serializer_class(self.get_queryset(), many=True).data, status = status.HTTP_200_OK)
        

    def retrieve(self, request, pk = None):
        if self.get_queryset(pk):
            return Response(self.serializer_class(self.get_queryset(pk)).data)
        return Response({'mensaje':'compra no encontrada'}, status = status.HTTP_404_NOT_FOUND)"""

    def create(self, request):
        compra_claves = ['accion','id_proveedor','id_empleado','monto_total','detalles']
        compra_valores = list(map(request.data.get,compra_claves))
       

        compra = cargar_datos(compra_claves,compra_valores)
        print(compra_valores)
        print(compra)
       
        if len(compra['detalles']) == 0:
            return Response({'message':'Por favor, complete los datos necesarios para realizar la compra'},status = status.HTTP_400_BAD_REQUEST)
        else:
            compra_serializer = CreateCompraSerializer(data =compra)
            if compra_serializer.is_valid():
                compra_serializer.save()
                detalle_compra = carga_detalle_compra(compra_claves,compra_valores,Compra,"detalles","id_compra")
                compra_delete = Compra.objects.latest('id')
                print(compra_delete)

                detalle_compra_serializer = DetalleCompraSerializer(data=detalle_compra, many=True)
                
                if detalle_compra_serializer.is_valid():    
                    detalle_compra_serializer.save()
                    return Response({'message':'Se ha creado la compra con éxito'}, status = status.HTTP_200_OK)
                compra_delete.delete()
                return Response(detalle_compra_serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
            else:
                return Response(compra_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

            

    def update(self, request, pk=None):
        queryset = Compra.objects.all().filter(id=pk).first()
        print(queryset)
        compra_serializer = CreateCompraSerializer(queryset,data = request.data)
        if compra_serializer.is_valid():
            compra_serializer.save()
            return Response(compra_serializer.data, status = status.HTTP_200_OK)
        return Response({compra_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

        
        
    
    def destroy(self,request, pk=None):
        compra_query = Compra.objects.filter(state = True,id=pk).first()
        detalle_compra_query = DetalleCompra.objects.filter(state = True, id_compra=pk)

        
        if compra_query and detalle_compra_query:
            compra_query.state=False
            compra_query.save()
            for detalle_only_query in detalle_compra_query:
                query_detalle = DetalleCompra.objects.filter(id=detalle_only_query.id).first()
                query_detalle.state = False
                query_detalle.save()
            return Response({'mensaje': 'Compra eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'mensaje': 'No existe esa compra'}, status = status.HTTP_400_BAD_REQUEST)