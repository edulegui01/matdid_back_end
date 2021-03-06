from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from apps.empleados.models import Empleado


class UsuarioManager(BaseUserManager):
    def _create_user(self, username, name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name, password=None, **extra_fields):
        return self._create_user(username, name, password, False, False, **extra_fields)

    def create_superuser(self, username, name, password=None, **extra_fields):
        return self._create_user(username, name, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    historical = HistoricalRecords()
    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'{self.name}'
