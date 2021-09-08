from rest_framework.routers import DefaultRouter
from apps.compras.views.compras_views import ComprasViewSet

router = DefaultRouter()

router.register(r'compras',ComprasViewSet, basename = 'compras')

urlpatterns = router.urls