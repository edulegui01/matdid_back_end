from ast import Return
from rest_framework import viewsets,status
from rest_framework.response import Response
from apps.productos.serializers.productos_serializers import ProductoSerializer
from apps.productos.serializers.productos_all_serializer import ProductoAllSerializer
from apps.productos.models import Producto

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True).order_by('-id')



    def create(self,request):
        producto_serializer = ProductoSerializer(data=request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response({'message':'El producto se creo con éxito.'},status = status.HTTP_200_OK)
        return Response(producto_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk):
        query_all = Producto.objects.filter(state = True, id = pk).first()
        producto_retrive_serializer = ProductoAllSerializer(query_all)

        return Response(producto_retrive_serializer.data,status = status.HTTP_200_OK)


    def update(self, request, pk):
        query_edit_product = Producto.objects.filter(state = True, id=pk).first()
        product_serializer_edit = ProductoSerializer(query_edit_product,data=request.data)
        if product_serializer_edit.is_valid():
            product_serializer_edit.save()
            return Response({'message':'El producto se ha editado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'No se pudo editar el producto'})

    def destroy(self,request, pk=None):
        query_producto_delete = Producto.objects.filter(id=pk).first()
        print(query_producto_delete.state)
        
        if query_producto_delete:
            query_producto_delete.state = False
            query_producto_delete.save()
            return Response({'mensaje':'Producto eliminado'},status = status.HTTP_200_OK)
        return Response({'mensaje':'No existe ese producto'},status = status.HTTP_400_BAD_REQUEST)