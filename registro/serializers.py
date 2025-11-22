from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Visita


class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Visita
        fields = [
            "url",
            "id",
            "nombre",
            "rut",
            "motivo",
            "hora_entrada",
            "hora_salida",
        ]

    def validate(self, attrs):
        hora_entrada = attrs.get("hora_entrada") or getattr(self.instance, "hora_entrada", None)
        hora_salida = attrs.get("hora_salida") or getattr(self.instance, "hora_salida", None)
        if hora_entrada and hora_salida and hora_salida < hora_entrada:
            raise serializers.ValidationError({
                "hora_salida": "La hora de salida debe ser mayor o igual a la hora de entrada."
            })
        return attrs

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

