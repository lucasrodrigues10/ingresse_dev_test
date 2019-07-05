from rest_framework.viewsets import ModelViewSet

from companies.api.serializers import CompanySerializer
from companies.models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
