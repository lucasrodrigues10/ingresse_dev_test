from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from candidates.api.serializers import CandidateSerializer
from candidates.models import Candidate


class CandidateViewSet(ModelViewSet):
    serializer_class = CandidateSerializer
    filter_backends = (SearchFilter,)
    # permission_classes = (IsAuthenticated,)  # IsAdminUser
    # authentication_classes = (TokenAuthentication,)
    search_fields = ('name', 'location__street')
    queryset = Candidate.objects.all()

    # def get_queryset(self):
    #     return super(CandidateViewSet, self).get_queryset()

    def list(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CandidateViewSet, self).partial_update(request, *args, **kwargs)
