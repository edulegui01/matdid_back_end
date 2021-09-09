from rest_framework import viewsets
from apps.productos.serializers.productos_serializers import ProductoSerializer

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = serializer_class.Meta.model.objects.all()