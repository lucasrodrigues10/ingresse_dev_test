from rest_framework.viewsets import ModelViewSet

from feedbacks.api.serializers import FeedbackSerializer
from feedbacks.models import Feedback


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
