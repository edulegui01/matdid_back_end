from rest_framework.routers import DefaultRouter
from apps.ventas.views.venta_view import VentasViewsSet
from apps.ventas.views.detalle_venta_edit_view import DetalleCompraEditView
from apps.ventas.views.venta_edit_view import VentasEditViewset
from apps.ventas.views.venta_grafica_view import VentasGraficaViewset

router = DefaultRouter()

router.register(r'ventas',VentasViewsSet,basename='ventas')
router.register(r'ventas_edit',VentasEditViewset,basename = 'ventas_edit')
router.register(r'detalle_venta_edit',DetalleCompraEditView,basename = 'detalle_venta_edit')
router.register(r'venta_grafica',VentasGraficaViewset,basename='venta_grafica')

urlpatterns = router.urls