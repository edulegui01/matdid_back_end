from rest_framework import viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.proveedores.serializers.proveedores_serializers import ProveedorSerializer
from apps.proveedores.serializers.proveedor_all_serializer import ProveedorAllSerializer
from apps.proveedores.models import Proveedor
from apps.proveedores.serializers.proveedores_serializers import ProveedorSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter(state = True).order_by('-id')


    def create(self,request):
        proveedor_serializer = ProveedorSerializer(data=request.data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response({'message':'El proveedor se creo con éxito.'},status = status.HTTP_200_OK)
        return Response(proveedor_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk):
        query_all = Proveedor.objects.filter(state = True, id = pk).first()
        proveedor_retrive_serializer = ProveedorAllSerializer(query_all)

        return Response(proveedor_retrive_serializer.data,status = status.HTTP_200_OK)


    def update(self, request, pk):
        query_edit_product = Proveedor.objects.filter(state = True, id=pk).first()
        product_serializer_edit = ProveedorSerializer(query_edit_product,data=request.data)
        if product_serializer_edit.is_valid():
            product_serializer_edit.save()
            return Response({'message':'El proveedor se ha editado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'No se pudo editar el proveedor'})

    def destroy(self,request, pk=None):
        query_proveedor_delete = Proveedor.objects.filter(id=pk).first()
        print(query_proveedor_delete.state)
        
        if query_proveedor_delete:
            query_proveedor_delete.state = False
            query_proveedor_delete.save()
            return Response({'mensaje':'proveedor eliminado'},status = status.HTTP_200_OK)
        return Response({'mensaje':'No existe ese proveedor'},status = status.HTTP_400_BAD_REQUEST)