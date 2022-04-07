from rest_framework.routers import DefaultRouter
from apps.compras.views.compras_views import ComprasViewSet
from apps.compras.views.compra_edit_view import ComprasEditViewset
from apps.compras.views.detalle_compra_edit_view import DetalleCompraEditView
from apps.compras.views.compras_update_view import CompraUpdateViewSet

router = DefaultRouter()

router.register(r'compras',ComprasViewSet, basename = 'compras')
router.register(r'compras_edit',ComprasEditViewset,basename = 'compras_edit')
router.register(r'detalle_compra_edit',DetalleCompraEditView,basename = 'detalle_compra_edit')
router.register(r'update_compra',CompraUpdateViewSet,basename = 'update_compra')

urlpatterns = router.urls