from rest_framework.serializers import ModelSerializer

from candidates.models import Candidate


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'cpf', 'name', 'gender')
