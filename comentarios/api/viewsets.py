from rest_framework import viewsets
from comentarios.models import Comentario
from comentarios.api.serializers import ComentarioSerializer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer