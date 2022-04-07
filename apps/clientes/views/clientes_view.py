from rest_framework import viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.clientes.models import Cliente
from apps.clientes.serializers.clientes_serializer import ClienteSerializer
from apps.clientes.serializers.cliente_all_serializer import ClienteAllSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter(state = True).order_by('-id')


    def create(self,request):
        cliente_serializer = ClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response({'message':'El cliente se creo con éxito.'},status = status.HTTP_200_OK)
        return Response(cliente_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk):
        query_all = Cliente.objects.filter(state = True, id = pk).first()
        cliente_retrive_serializer = ClienteAllSerializer(query_all)

        return Response(cliente_retrive_serializer.data,status = status.HTTP_200_OK)


    def update(self, request, pk):
        query_edit_product = Cliente.objects.filter(state = True, id=pk).first()
        product_serializer_edit = ClienteSerializer(query_edit_product,data=request.data)
        if product_serializer_edit.is_valid():
            product_serializer_edit.save()
            return Response({'message':'El cliente se ha editado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'No se pudo editar el cliente'})

    def destroy(self,request, pk=None):
        query_cliente_delete = Cliente.objects.filter(id=pk).first()
        print(query_cliente_delete.state)
        
        if query_cliente_delete:
            query_cliente_delete.state = False
            query_cliente_delete.save()
            return Response({'mensaje':'cliente eliminado'},status = status.HTTP_200_OK)
        return Response({'mensaje':'No existe ese cliente'},status = status.HTTP_400_BAD_REQUEST)