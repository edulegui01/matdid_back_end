from rest_framework.routers import DefaultRouter
from apps.productos.views.producto_view import ProductoView
from apps.productos.views.productos_compra_view import ProductoCompraViewSet

router = DefaultRouter()

router.register(r'productos',ProductoView,basename = 'productos')
router.register(r'productos_compra',ProductoCompraViewSet,basename = 'productos_compra')

urlpatterns=router.urls
