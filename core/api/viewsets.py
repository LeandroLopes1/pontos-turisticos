from rest_framework import viewsets
from core.models import PontoTuristico, Atracao
from .serializers import PontoTuristicoSerializer, AtracaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

class PontosTuristicosViewSet(viewsets.ModelViewSet):
  
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
 
    search_fields = ('nome', 'descricao', 'endereco__linha1')
 

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        if id:
            return PontoTuristico.objects.filter(id=id)
        if nome:
            return PontoTuristico.objects.filter(nome=nome)
        if descricao:
            return PontoTuristico.objects.filter(descricao=descricao)
        return PontoTuristico.objects.all()

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
        return Response({'teste': 'teste'})

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=pk)
        
        ponto.atracoes.set(atracoes)
        ponto.save()
        return Response({'message': 'Atracoes associadas com sucesso!'})

        
