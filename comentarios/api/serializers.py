from rest_framework import serializers
from comentarios.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ( 'usuario', 'comentario', 'data_comentario', 'aprovado')
