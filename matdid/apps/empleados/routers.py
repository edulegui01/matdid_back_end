from rest_framework.routers import DefaultRouter
from apps.empleados.views.empleados_compras_view import EmpleadosCompraViewSet

router= DefaultRouter()

router.register(r'empleados_compra',EmpleadosCompraViewSet,basename='empleados_compra')

urlpatterns=router.urls