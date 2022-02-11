from rest_framework import viewsets
from apps.productos.serializers.productos_compra_serializer import ProductoCompraSerializer

class ProductoCompraViewSet(viewsets.ModelViewSet):
    serializer_class=ProductoCompraSerializer
    queryset=serializer_class.Meta.model.objects.all()
    pagination_class = None 