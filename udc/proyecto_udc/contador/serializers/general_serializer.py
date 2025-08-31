from rest_framework import serializers
from ..models import Sala, Baliza, Evento, Sesion

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        exclude = ('state',)

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baliza
        exclude = ('state',)

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baliza
        exclude = ('state',)

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baliza
        exclude = ('state',)


