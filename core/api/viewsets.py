from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PontosTuristicosViewSet(viewsets.ModelViewSet):
  
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
       return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
        return Response({'teste': 'teste'})

   