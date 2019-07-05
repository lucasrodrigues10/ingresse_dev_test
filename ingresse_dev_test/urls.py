from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from candidates.api.viewsets import CandidateViewSet
from companies.api.viewsets import CompanyViewSet
from feedbacks.api.viewsets import FeedbackViewSet
from locations.api.viewsets import LocationViewSet

router = routers.DefaultRouter()
router.register('candidates', CandidateViewSet, base_name='Candidate')
router.register('companies', CompanyViewSet, base_name='Company')
router.register('feedbacks', FeedbackViewSet, base_name='Feedback')
router.register('locations', LocationViewSet, base_name='Location')

urlpatterns = (
    [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path('api-token-auth', obtain_auth_token),
    ]
)
