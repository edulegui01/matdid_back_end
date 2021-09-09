from rest_framework.routers import DefaultRouter
from apps.clientes.views.cobros_view import CobrosViewSet

router = DefaultRouter()

router.register(r'cobros',CobrosViewSet,basename='cobros')

urlpatterns = router.urls