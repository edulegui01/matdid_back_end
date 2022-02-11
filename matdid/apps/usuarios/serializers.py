from rest_framework import serializers
from apps.usuarios.models import Usuario


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username','name')