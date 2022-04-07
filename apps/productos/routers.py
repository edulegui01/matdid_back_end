from rest_framework.routers import DefaultRouter
from apps.productos.views.producto_view import ProductoView
from apps.productos.views.productos_compra_view import ProductoCompraViewSet
from apps.productos.views.producto_all_view import ProductoAllView

router = DefaultRouter()

router.register(r'productos',ProductoView,basename = 'productos')
router.register(r'productos_compra',ProductoCompraViewSet,basename = 'productos_compra')
router.register(r'productos_edit',ProductoAllView,basename = 'productos_edit')


urlpatterns=router.urls
