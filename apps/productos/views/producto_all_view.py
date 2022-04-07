from ast import Return
from rest_framework import viewsets,status
from rest_framework.response import Response
from apps.productos.serializers.productos_serializers import ProductoSerializer
from apps.productos.serializers.productos_all_serializer import ProductoAllSerializer
from apps.productos.models import Producto


class ProductoAllView(viewsets.ModelViewSet):
    serializer_class = ProductoAllSerializer
    queryset = Producto.objects.filter(state = True)