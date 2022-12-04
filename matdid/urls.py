
from django.contrib import admin
from django.urls import path, include
from apps.usuarios.views import Login,Logout,UserToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedores/',include('apps.proveedores.routers')),
    path('compras/',include('apps.compras.routers')),
    path('productos/',include('apps.productos.routers')),
    path('',Login.as_view(),name='Login'),
    path('logout/',Logout.as_view(),name='Logout'),
    path('refresh-token/',UserToken.as_view(),name='refresh_token'),
    path('ventas/',include('apps.ventas.routers')),
    path('cobros/',include('apps.clientes.routers')),
    path('empleados/',include('apps.empleados.routers')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
