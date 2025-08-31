from rest_framework import serializers
from notes.models import Notas


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        exclude = ('state',)