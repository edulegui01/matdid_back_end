from rest_framework.routers import DefaultRouter
from apps.clientes.views.cobros_view import CobrosViewSet
from apps.clientes.views.clientes_venta_view import ClientesVentaViewSet
router = DefaultRouter()

router.register(r'cobros',CobrosViewSet,basename='cobros')
router.register(r'clientes_venta',ClientesVentaViewSet,basename='clientes_venta')

urlpatterns = router.urls