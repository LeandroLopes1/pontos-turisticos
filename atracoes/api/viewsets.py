from rest_framework import viewsets
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AtracoesViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('nome', 'descricao')
