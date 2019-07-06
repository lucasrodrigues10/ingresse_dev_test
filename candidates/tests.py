from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CandidateTest(APITestCase):
    def test_candidate_not_found(self):
        data = {'name': 'jorge'}
        response = self.client.get(reverse('candidates'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_candidate_found(self):
        data = {'name': 'lucas'}
        response = self.client.get(reverse('candidates'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
