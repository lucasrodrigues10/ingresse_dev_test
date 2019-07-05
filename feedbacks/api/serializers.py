from rest_framework.serializers import ModelSerializer

from feedbacks.models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('user', 'description', 'rating', 'date')
