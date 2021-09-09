from rest_framework.routers import DefaultRouter
from apps.proveedores.views.proveedores_view import ProveedorViewSet
from apps.proveedores.views.proveedores_compra_view import ProveedoresCompraViewSet

router = DefaultRouter()

router.register(r'proveedores',ProveedorViewSet, basename = 'proveedores')
router.register(r'proveedores_compra',ProveedoresCompraViewSet,basename='proveedores_compra')

urlpatterns = router.urls