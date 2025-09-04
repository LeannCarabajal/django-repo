from rest_framework import serializers
from ..models import Sala, Baliza, Sesion

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        exclude = ('state',)

class BalizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baliza
        exclude = ('state',)

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesion
        exclude = ('state',)


