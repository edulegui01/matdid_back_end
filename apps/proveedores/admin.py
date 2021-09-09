from django.contrib import admin
from apps.proveedores.models import Proveedor
from apps.proveedores.models import Pago
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Pago)


