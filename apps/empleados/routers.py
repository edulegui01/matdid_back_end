from rest_framework.routers import DefaultRouter
from apps.empleados.views.empleados_compras_view import EmpleadosCompraViewSet
from apps.empleados.views.empleados_veiw import EmpleadoViewSet
from apps.empleados.views.empleados_all_view import EmpleadoAllView

router= DefaultRouter()

router.register(r'empleados_compra',EmpleadosCompraViewSet,basename='empleados_compra')
router.register(r'empleados',EmpleadoViewSet,basename='empleados')
router.register(r'empleados_edit',EmpleadoAllView,basename='empleados_edit')

urlpatterns=router.urls