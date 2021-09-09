from rest_framework.routers import DefaultRouter
from apps.productos.views.producto_view import ProductoView

router = DefaultRouter()

router.register(r'productos',ProductoView,basename = 'productos')

urlpatterns=router.urls
