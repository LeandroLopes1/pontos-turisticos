from rest_framework import serializers
from avaliacoes.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('usuario', 'comentario', 'nota', 'data')
      