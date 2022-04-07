from rest_framework.routers import DefaultRouter
from apps.clientes.views.cobros_view import CobrosViewSet
from apps.clientes.views.clientes_venta_view import ClientesVentaViewSet
from apps.clientes.views.clientes_view import ClienteViewSet
router = DefaultRouter()

router.register(r'cobros',CobrosViewSet,basename='cobros')
router.register(r'clientes_venta',ClientesVentaViewSet,basename='clientes_venta')
router.register(r'clientes_venta',ClientesVentaViewSet,basename='clientes_venta')
router.register(r'clientes',ClienteViewSet,basename='clientes')

urlpatterns = router.urls