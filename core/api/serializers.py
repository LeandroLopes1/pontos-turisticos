from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico, Atracao, Endereco, DocIdenticacao
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class DocIdenticacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdenticacao
        fields = '__all__'

class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(many=False)
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdenticacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 
            'comentarios', 'avaliacoes', 'endereco', 'atracoes', 'descricao_completa',
            'descricao_completa2', 'doc_identificacao'
        )
        read_only_fields = ('comentarios', 'avaliacoes')
    
  
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        endereco = validated_data['endereco']
        del validated_data['endereco']
        doc_identificacao = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdenticacao.objects.create(**doc_identificacao)

        ponto = PontoTuristico.objects.create(**validated_data)
        for atracao in atracoes:
            atracao_obj = Atracao.objects.create(**atracao)
            ponto.atracoes.add(atracao_obj)

        endereco_obj = Endereco.objects.create(**endereco)
        ponto.endereco = endereco_obj
        ponto.doc_identificacao = doci
        ponto.save()
       
        return ponto
  
       
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)