from rest_framework.routers import DefaultRouter
from apps.ventas.views.venta_view import VentasViewsSet

router = DefaultRouter()

router.register(r'ventas',VentasViewsSet,basename='ventas')

urlpatterns = router.urls